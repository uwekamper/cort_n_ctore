root = this

class root.MainRouter extends Backbone.Router

  routes:
    '':  'show'

  initialize: (options) ->
    console.log('init router')

  show: ->
    console.log('show')
    alert('bla')


jQuery(document).ready ->
  quiz = new root.MainRouter()
  Backbone.history.start
