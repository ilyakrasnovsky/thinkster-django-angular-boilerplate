//high level module
//dependencies are thinkster.routes and thinkster.authentication
(function () {
  'use strict';

  angular
    .module('thinkster', [
      'thinkster.config',
      'thinkster.routes',
      'thinkster.authentication'
    ]);

  angular
    .module('thinkster.routes', ['ngRoute']);
    
  angular
  	.module('thinkster.config', []);
})();
