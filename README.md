SublimeLinter-jscs
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-jscs.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-jscs)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [jscs](https://github.com/mdevils/node-jscs).


## Installation

SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before using this plugin, ensure that `jscs` (1.0.10 or later, 1.9.0 or later for JSX support) is installed on your system.
To install `jscs`, do the following:

1. Install [Node.js](http://nodejs.org) (and [npm](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager) on Linux).

1. Install `jscs` by typing the following in a terminal:
   ```
   npm install -g jscs
   ```

1. If you are using `nvm` and `zsh`, ensure that the line to load `nvm` is in `.zshenv` and not `.zshrc`.

1. If you are using `zsh` and `oh-my-zsh`, do not load the `nvm` plugin for `oh-my-zsh`.


Please make sure that the path to `jscs` is available to SublimeLinter.
The docs cover [troubleshooting PATH configuration](http://sublimelinter.com/en/latest/troubleshooting.html#finding-a-linter-executable).


## Settings

- SublimeLinter settings: http://sublimelinter.com/en/latest/settings.html
- Linter settings: http://sublimelinter.com/en/latest/linter_settings.html

Since this plugin is executing `jscs` on your system, you may use `.jscsrc` files to configure its behavior. See the [jscs documentation](http://jscs.info/overview.html#options) for more information.

If you wish to run against `jsx` files, you will need to install [esprima-fb](https://www.npmjs.com/package/esprima-fb)
with `npm install -g esprima-fb` add the following lines to your `.jscsrc` file:

```json
...
    "esprima": "esprima-fb",
    "fileExtensions": [".js", ".jsx"],
...
```
