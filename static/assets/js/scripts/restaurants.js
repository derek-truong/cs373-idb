// tutorial8.js
var data = [
  {id: 1, rname: "Pete Hunt", text: "This is one restaurant"},
  {id: 2, rname: "Jordan Walke", text: "This is *another* restaurant"}
];

var RestaurantTable = React.createClass({
  render: function() {
    return (
      <div className="restaurantTable">
        <h1>Restaurants</h1>
        <RestaurantList data={this.props.data} />
      </div>
    );
  }
});

var RestaurantList = React.createClass({
  render: function() {
    var restaurantNodes = this.props.data.map(function(restaurant) {
      return (
        <Restaurant rname={restaurant.rname} key={restaurant.id}>
          {restaurant.text}
        </Restaurant>
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
      // <div className="restaurant">
        // <h2 className="restaurantRname">
            <tr>
	            <td data-search="0">0</td>
	            <td><a href="/restaurants/0">Eggslut</a></td>
	            <td>Los Angeles</td>
	            <td>4.2</td>
	            <td>Breakfast &amp; Brunch</td>
	            <td>317 S BroadwayLos Angeles, CA 90013</td>
        	</tr>
          // {this.props.rname}
        // </h2>
        // {this.props.children}
      // </div>
    );
  }
});

ReactDOM.render(
  <RestaurantTable data={data} />,
  document.getElementById('content')
);

// var RestaurantList = React.createClass({
//   render: function() {
//     return (
//       <div className="restaurant">
//         <Table />
//       </div>
//     );
//   }
// });

//restaurantList
// tutorial9.js
// var RestaurantTable = React.createClass({
//   render: function() {
//     return (
//       <div className="restaurantTable">
//         <h1>Comments</h1>
//         <RestaurantList data={this.props.data} />
//         <CommentForm />
//       </div>
//     );
//   }
// });

// tutorial10.js
// var RestaurantList = React.createClass({
//   render: function() {
//     var restaurantNodes = this.props.data.map(function(restaurant) {
//       return (
//         <Restaurant rname={restaurant.rname} key={restaurant.id}>
//           {restaurant.text}
//         </Restaurant>
//       );
//     });
//     return (
//       <div className="restaurantList">
//         {restaurantNodes}
//       </div>
//     );
//   }
// });

// var RestaurantEntry = React.createClass({
//   render: function() {
//     return (
//       <div className="restaurantEntry">
//         <h2 className="restaurantEntryName">
//           {this.props.thename}
//         </h2>
//         {this.props.children}
//       </div>
//     );
//   }
// });

// var Search = React.createClass({
//   render: function() {
//     return (
//       <div className="search">
//         Hello, world! I am a Search.
//       </div>
//     );
//   }
// });

// ReactDOM.render(
//   <RestaurantList />,
//   document.getElementById('content')
// );


//                    <!-- <table id="example" class="display" cellspacing="0" width="100%">
//                         <thead>
//                             <tr>
//                                 <th>ID</th>
//                                 <th>Name</th>
//                                 <th>Location</th>
//                                 <th>Rating</th>
//                                 <th>Category</th>
//                                 <th>Address</th>
//                             </tr>
//                         </thead> -->
// <!--                         <tfoot>
//                             <tr>
//                                 <th>ID</th>
//                                 <th>Name</th>
//                                 <th>Location</th>
//                                 <th>Rating</th>
//                                 <th>Category</th>
//                                 <th>Address</th>
//                             </tr>
//                         </tfoot> -->
//                         <!-- <tbody>
//                             <tr>
//                                 <td data-search="0">0</td>
//                                 <td><a href="/restaurants/0">Eggslut</a></td>
//                                 <td>Los Angeles</td>
//                                 <td>4.2</td>
//                                 <td>Breakfast &amp; Brunch</td>
//                                 <td>317 S BroadwayLos Angeles, CA 90013</td>
//                             </tr>
//                             <tr>
//                                 <td data-search="1">1</td>
//                                 <td><a href="/restaurants/1">Cera 23</a></td>
//                                 <td>Barcelona</td>
//                                 <td>4.6</td>
//                                 <td>Spanish</td>
//                                 <td>Carrer de la Cera, 2308001 Barcelona, Spain</td>
//                             </tr>
//                             <tr>
//                                 <td data-search="2">2</td>
//                                 <td><a href="restaurants/2">Den Noc</a></td>
//                                 <td>Prague</td>
//                                 <td>4.4</td>
//                                 <td>Breakfast &amp; Brunch</td>
//                                 <td>110 00 Prague, Czech Republic</td>
//                             </tr>
//                         </tbody>
//                     </table>