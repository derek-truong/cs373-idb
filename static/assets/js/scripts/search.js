var SearchList = React.createClass({
  loadDataFromServer: function() {
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      cache: false,
      success: function(data) {

        this.setState({data: data});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  getInitialState: function() {
    return {data: []};
  },
  componentWillMount: function() {
    this.loadDataFromServer();
  },
  render: function() {
    var searchNodes = this.state.data.map(function(search) {
      return (<SearchItem search_ob={search}/>);
    });
    return (
        <div>
          {searchNodes}
        </div>
    );
  }
});


var SearchItem = React.createClass({
  render: function() {
    return (
      <p>
      <a href={this.props.search_ob.link}>{this.props.search_ob.name}</a>
      {this.props.search_ob.description}
      </p>

    );
  }
});

function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}
var query=getParameterByName('search');
var str1 = "/api/search/";
var str2 = str1.concat(query)
console.log(str2);
ReactDOM.render(
    <SearchList url = {str2}/>,
    document.getElementById('content')
);