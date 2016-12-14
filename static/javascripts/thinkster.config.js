//thinkster.config module
(function () {
  'use strict';

  angular
    .module('thinkster.config')
    .config(config);

  config.$inject = ['$locationProvider'];

  /**
  * @name config
  * @desc Enable HTML5 routing
  */
  //gets rid of hash routing (except for pre-HTML5 browsers)
  //and replaces the hash prefix with #! for the benefit of
  //search engines
  function config($locationProvider) {
    $locationProvider.html5Mode(true);
    $locationProvider.hashPrefix('!');
  }
})();