For npm scripts, NPM supports env variables in the form $npm_package_config_var, for example.  This can be used in `npm run` commands.  However, this is platform specific.  Windows uses %var% where \*nix uses $var.  This tool can be run like:

> compat 'ncp $sourcePath $destPath'

so that, on windows platforms, the following command will be run:

> ncp %sourcePath% %destPath%
