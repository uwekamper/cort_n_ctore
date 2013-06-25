
var Part = Backbone.Model.extend({
    defaults: {
        name: ''
    },

    initialize: function(){
        console.log('This Part model has been initialized.');
    }
});

var PartsCollection = Backbone.Collection.extend({
  model: Part,
  url: '/inventory/parts/'
});

var Place = Backbone.Model.extend({
    defaults: {
        name: 'Place with no name',
        parent: null,
        type: 'Unknown'
    },

    initialize: function(){
        console.log('This Place model has been initialized.');
    }
});

var PartView = Backbone.View.extend({
    tagName: 'tr',
    partTpl: $('#partTpl').html(),

    events: {
        'click .editBtn': 'edit'
    },

    initialize: function() {
      this.listenTo(this.model, "change", this.render);
    },
    render: function() {
        this.$el.html( Mustache.render(this.partTpl, this.model.toJSON()) );
        return this;
    },
    edit: function() {
        router.navigate('#edit/' + parts.indexOf(this.model), true);
    }
});

var PartsListView = Backbone.View.extend({
    tagName: 'tbody',

    itemViews: {},

    initialize: function(options) {
      this.collection = options.collection;
      this.listenTo(this.collection, "add", this.renderItem);
      this.listenTo(this.collection, "remove", this.removeItem);
      this.listenTo(this.collection, "reset", this.render);
    },

    render: function(){
        this.$el.empty();
        this.collection.each(this.renderItem, this);
        return this;
    },

    renderItem: function (item) {
        var itemView = new PartView({ model: item });
        this.$el.append( itemView.render().el );
        this.itemViews[item.id] = itemView;
    }
});

// pass array of models on collection instantiation
var parts = new PartsCollection();

var PartEditView = Backbone.View.extend({
    tagName: 'div',

    initialize: function(options) {
        this.part = options.part;
        this.listenTo(this.collection, "reset", this.render);
    },

    render: function() {
        this.$el.append();
        return this;
    }
});

var PartsRouter = Backbone.Router.extend({
    routes: {
        "edit/:idx": "editRoute",
        "": "defaultRoute"
    },

    defaultRoute: function() {
        var partslistview = new PartsListView({collection: parts});
        $('#searchresultstable').append(partslistview.render().el);
        parts.fetch({ reset: true });
    },

    editRoute: function() {
        idx = 1
        var part = parts.get(idx);
        var partEditView = new PartEditView({model: part});
        $('#searchresultstable').empty();
        $('#searchresultstable').append(partEditView.render().el);
        alert("vla");
    }

});

router = new PartsRouter();

$(document).ready(function () {
     Backbone.history.start();
});
