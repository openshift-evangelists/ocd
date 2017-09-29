# ocd - OpenShift for developers

`ocd` is command line tool designed for engineers working with OpenShift

This is a proof of concept and not meant to be used for 'real' work.

## Installation

To get started clone the git repo and source the entrypoint.sh script

```
$ git clone https://github.com/openshift-evangelists/ocd.git
$ source ocd/entrypoint.sh
```

## Requirements

Most of the commands require just `oc` and `bash`, though, some have external dependencies

### ocd link

Requires also 

* [`jq`](https://stedolan.github.io/jq/)
* `sed`
* `awk`
* `base64`

## Help

### ocd app [name]

Creates new application context. 

`name` is mandatory.

Will create project `name` if not project currently selected.

### ocd create [type] [name] [path]

Deploy new thing of type `type` and name it `name`. 

`type` is mandatory. `name` defaults to `type` when no specified. `path` is manadatory for s2i apps.

`oc create mysql` is equivalent to `oc create mysql mysql`, will create new deployment from the `mysql` temaplate with name `mysql`.

`oc create php php <url>` will create new deployment using `php` from source code `<url>`.

### ocd deploy [name] [path]

Triggers new build.

`name` is mandatory.

`path` is mandatory for `--from-dir` builds.

### ocd sync [name] [path]

Start rsync to the pod. Will take first running pod for deployment `name`.

`name` is mandatory. `path` defaults to `.`.

### ocd link [name] [target]

Expects to find secret with name `name`, create e.g. my MySQL template, and copies the values as ENV to `target`.

`name` and `target` are mandatory.

### ocd storage add [type] [size] [path] [name]

Adds new persistent `local or shared` storage of `size` to deployment `name` mounted at `path`.

`type` is mandatory and is either `shared` or `local`. `size`, `path` and `name` are mandatory.

### ocd url add [name]

Create route for deployment `name`.

`name` is mandatory.

### ocd scale [count] [name]

Scale deployment `name` to `count` pods.

`name` and `count` are mandatory.

### ocd destroy [name]

Undeploy deployment `name`.

`name` is mandatory.

### ocd wipe

Delete all deployments in current application context.

### ocd exit

Exit the application context.

## How to

After installation the `ocd` command is available to use.

## License

`ocd` is released under the MIT License.
