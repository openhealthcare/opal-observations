module.exports = function(config){
  var opalPath = process.env.OPAL_LOCATION;
  var karmaDefaults = require(opalPath + '/opal/tests/js_config/karma_defaults.js');
  var baseDir = __dirname + '/..';
  var coverageFiles = [
    __dirname+'/../obs/static/js/obs/**/*.js'
  ];
  var includedFiles = [
    "lib/d3/d3.js",
    "lib/c3-0.4.10/c3.js",
    __dirname+'/../obs/static/js/obs/controllers/*.js',
    __dirname+'/../obs/static/js/obs/services/**/*.js',
    __dirname+'/../obs/static/js/test/*.js',
  ];

  var defaultConfig = karmaDefaults(includedFiles, baseDir, coverageFiles);
  config.set(defaultConfig);
};
