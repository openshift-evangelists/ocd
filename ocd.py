import click
import os
import subprocess

context_file = os.path.expanduser("~/.ocd/context")


def run(cmd, stdin=None):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    if stdin is not None:
        stdout, stderr = process.communicate(stdin.encode('utf-8'))
        return [process.returncode, stdout, stderr]
    else:
        return [process.returncode, process.stdout.read().decode('utf-8'), process.stderr.read().decode('utf-8')]


def context():
    with open(context_file, "r") as file:
        return file.read()


@click.group()
def cli():
    pass


@cli.command(name='shell-init')
def shell_init():
    """Enhance your shell with ocd"""
    path = os.path.dirname(os.path.abspath(__file__))
    script = """
#!/bin/bash
mkdir -p $HOME/.ocd
export OCD_PROJECT='$(oc project -q)'
export OCD_CONTEXT='$([ -f $HOME/.ocd/context ] && echo "/`cat $HOME/.ocd/context`")'
export PS1="[$OCD_PROJECT$OCD_CONTEXT] $PS1"
alias ocd="python3 %s/ocd.py"
    """ % path
    print(script)

@cli.command()
@click.argument('name')
def app(name):
    """Enter context"""
    with open(context_file, "w") as file:
        file.write(name)


@cli.command()
@click.argument('type')
@click.argument('name', required=False)
@click.argument('source', required=False)
def create(type, name, source):
    """Create component"""
    if name is None:
        name = type

    if source is None:
        run(["oc", "new-app", type, "--name", name, "--param=DATABASE_SERVICE_NAME=%s" % name, "-lapp=%s" % context()])
    else:
        run(["oc", "new-app", "%s~%s" % (type, source), "--name", name, "-lapp=%s" % context()])


@cli.command()
@click.argument('name')
@click.argument('source', required=False)
def deploy(name, source):
    """Trigger component deployment"""
    if source is None:
        run(["oc", "start-build", name])
    else:
        run(["oc", "start-build", name, "--from-dir=%s" % source])


@cli.command()
@click.argument('name')
def destroy(name):
    """Destroy component"""
    run(["oc", "delete", "all", "-lapp=%s" % name])
    run(["oc", "delete", "pvc", name])
    run(["oc", "delete", "secret", name])


@cli.command()
def exit():
    """Exit context"""
    os.remove(context_file)


@cli.command()
@click.argument('name')
def expose(name):
    """Expose component"""
    run(['oc', 'expose', 'service', name])


@cli.command()
@click.argument('source')
@click.argument('target')
def link(source, target):
    """Link components"""
    print(run(['oc', 'set', 'env', 'dc', target, '--from=secret/%s' % source]))


@cli.command()
@click.argument('count')
@click.argument('name')
def scale(count, name):
    """Scale component"""
    print(run(['oc', 'scale', 'dc', name, "--replicas=%s" % count]))


@cli.group()
def storage():
    """Manage persistent storage"""
    pass


@storage.command(name="add")
@click.argument('type')
@click.argument('size')
@click.argument('target')
@click.argument('name')
def storage_add(type, size, target, name):
    """Add persistent storage"""
    if type == 'shared':
        type = 'ReadWriteMany'

    if type == 'local':
        type = 'ReadWriteOnce'

    yml = """
apiVersion: "v1"
kind: "PersistentVolumeClaim"
metadata:
  name: %s
spec:
  accessModes:
    - %s
  resources:
    requests:
      storage: %s
  volumeName: %s
""" % (name, type, size, name)

    run(['oc', 'create', '-f', '-'], yml)
    run(['oc', 'volume', 'dc', name, '--add', '--type=persistentVolumeClaim', '--mount-path=%s' % target, '--claim-name=%s' % name])


@cli.command()
@click.argument('name')
@click.argument('source', required=False)
def sync(name, source):
    """Sync data to component"""
    if source is None:
        source = "."

    code, out, err = run(['oc', 'get', 'pods', '-ldeploymentconfig=%s' % name, '-o', 'name'])
    pods = out.strip().split('\n')
    pod = pods[0][5:]

    print(run(['oc', 'rsync', '--watch=true', source, '%s:.' % pod]))


@cli.command()
@click.argument('name', required=False)
def wipe(name):
    """Wipe components in context"""
    if name is None:
        name = context()

    code, out, err = run(['oc', 'get', 'dc', '-lapp=%s' % name, '-o', 'name'])
    dcs = out.strip().split('\n')
    for dc in dcs:
        dc = dc[18:]
        run(['oc', 'delete', 'secret', dc])
        run(['oc', 'delete', 'pvc', dc])

    run(['oc', 'delete', 'all', '-lapp=%s' % name])

if __name__ == '__main__':
    os.environ["LC_ALL"] = "en_US.UTF-8"
    os.environ["LANG"] = "en_US.UTF-8"
    cli()