// tutorial8.js

var data = [
  {id: 1, rname: "Pete Hunt", text: "This is one restaurant"},
  {id: 2, rname: "Jordan Walke", text: "This is *another* restaurant"}
];

var RestaurantTable = React.createClass({
  render: function() {
    return (
        <RestaurantList data={this.props.data} />
    );
  }
});

var RestaurantList = React.createClass({
  render: function() {
    var restaurantNodes = this.props.data.map(function(restaurant) {
      return (
        <Restaurant rname={restaurant.rname} key={restaurant.id}/>
      );
    });
    return (
      <div className="restaurantList">
        {restaurantNodes}
      </div>
    );
  }
});


var Restaurant = React.createClass({
  render: function() {
    return (
          <tr>
	            <td data-search="0">0</td>
	            <td><a href="/restaurants/0">Eggslut</a></td>
	            <td>Los Angeles</td>
	            <td>4.2</td>
	            <td>Breakfast &amp; Brunch</td>
	            <td>317 S BroadwayLos Angeles, CA 90013</td>
        	</tr>
    );
  }
});

ReactDOM.render(
  <RestaurantTable data={data} />,
  document.getElementById('content')
);

