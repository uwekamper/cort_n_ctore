app = this

models = {}


class models.Part extends Backbone.Model
  defaults:
    name: ''

  initialize: (options) ->
    console.log 'This Part model has been initialized.'


class models.PartsCollection extends Backbone.Collection
  model: models.Part
  url: '/inventory/parts/'


class models.Place extends Backbone.Model
  defaults:
    name: 'Place with no name',
    parent: null,
    type: 'Unknown'

  initialize: (options) ->
    console.log('This Place model has been initialized.')

app.models = models

views = {}

class views.PartView extends Backbone.View
  tagName: 'tr'
  partTpl: jQuery('#partTpl').html()
#  events:
#    'click .editBtn': 'edit'

  initialize: (options) ->
    this.listenTo(this.model, "change", this.render)

  render: ->
    this.$el.html( Mustache.render(this.partTpl, this.model.toJSON()) )
    return this

#  edit: ->
#    router.navigate('#edit/' + parts.indexOf(this.model), true)

class views.PartsListView extends Backbone.View
  tagName: 'tbody'

  itemViews: {}

  initialize: (options) ->
    this.collection = options.collection
    this.listenTo(this.collection, "add", this.renderItem)
    this.listenTo(this.collection, "remove", this.removeItem)
    this.listenTo(this.collection, "reset", this.render)

  render: ->
    this.$el.empty()
    this.collection.each(this.renderItem, this)
    return this

  renderItem: (item) ->
    itemView = new views.PartView({ model: item })
    this.$el.append( itemView.render().el )
    this.itemViews[item.id] = itemView


class views.PartEditView extends Backbone.View
  tagName: 'div'

  initialize: (options) ->
    this.part = options.part
    this.listenTo(this.collection, "reset", this.render)

  render: ->
    this.$el.append()
    return this

app.views = views

routers = {}

class routers.PartsRouter extends Backbone.Router
  routes:
    '': 'defaultRoute'

  defaultRoute: ->
    console.log('blaaah')
    partslistview = new views.PartsListView {collection: app.parts}
    jQuery('#searchresultstable').append(partslistview.render().el)
    parts.fetch({ reset: true })

app.models = models
app.views = views
app.routers = routers


jQuery(document).ready ->
  app.parts = new app.models.PartsCollection
  app.main_route = new app.routers.PartsRouter()
  Backbone.history.start()