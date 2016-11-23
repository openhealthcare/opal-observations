module.exports = function(config){
  var opalPath;
  var projectName = "lab";
  if(process.env.TRAVIS){
    python_version = process.env.TRAVIS_PYTHON_VERSION;
    opalPath = '/home/travis/virtualenv/python' + python_version + '/src/opal';
  }
  else{
    opalPath = '../../opal';
  }
  var karmaDefaults = require(opalPath + '/config/karma_defaults.js');
  var karmaDir = __dirname;
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

  var defaultConfig = karmaDefaults(karmaDir, coverageFiles, includedFiles);
  config.set(defaultConfig);
};
