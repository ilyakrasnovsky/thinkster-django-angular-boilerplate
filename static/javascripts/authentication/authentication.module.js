//thinkster.authentication module
//kind of like __init__.py in this directory?
(function () {
  'use strict';

  //defines the thinkster.authentication module with
  //the thinkster.authentication.controllers and
  //thinkster.authentication.services as dependencies
  angular
    .module('thinkster.authentication', [
      'thinkster.authentication.controllers',
      'thinkster.authentication.services'
    ]);

   //same idea, .module(module_name, [dependencies])
  angular
    .module('thinkster.authentication.controllers', []);

  angular
    .module('thinkster.authentication.services', ['ngCookies']);

  //code below this point configures angular to include csrf tokes
  //required by ensure_csrf_token within the django view handling
  //the reqeust
  angular
  	.module('thinkster')
  	.run(run);

  run.$inject = ['$http'];

  /**
  * @name run
  * @desc Update xsrf $http headers to align with Django's defaults
  */
  function run($http) {
	  $http.defaults.xsrfHeaderName = 'X-CSRFToken';
	  $http.defaults.xsrfCookieName = 'csrftoken';
	}
})();