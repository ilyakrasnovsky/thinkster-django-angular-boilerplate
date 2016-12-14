//client-side routing module
(function () {
  'use strict';

  angular
    .module('thinkster.routes')
    .config(config); //allows us to edit Angular's configuration via the config function/object below

  //adding routeProvider (service) as a dependency
  config.$inject = ['$routeProvider'];

  /**
  * @name config
  * @desc Define valid application routes
  */
  //this is the client side version of urls.py?
  function config($routeProvider) {
    //routeProvider.when(path, options)
    //path is wrt to base app URL, so we want registration form to be under /register
    //options is json object, where you can set controller (defined in register.controller.js),
    //controllerAs is saying we want to refer to the controller as vm in the HTML template
    //templateURL is the path to the template HTML file for registration we wrote
    $routeProvider.when('/register', {
      controller: 'RegisterController', 
      controllerAs: 'vm',
      templateUrl: '/static/templates/authentication/register.html'
    }).otherwise('/'); //catch at the end, redirecting user to '/' if they entered an unsupported URL
  }
})();