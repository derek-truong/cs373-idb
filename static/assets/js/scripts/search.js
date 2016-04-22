function isEmptyObject( obj ) {
    for ( var name in obj ) {
        return false;
    }
    return true;
}

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
    console.log("IDK IF THIS WORK");
    this.loadDataFromServer();
  },
  render: function() {
    if(!isEmptyObject(this.state.data)){
      var searchOrNodes = this.state.data['or_results'].map(function(search) {
        return (<SearchItem search_ob={search}/>);});

      var searchAndNodes = this.state.data['and_results'].map(function(search) {
        return (<SearchItem search_ob={search}/>);});
    }
      return (
        <div>
        <h4>Or Results</h4>
        <hr/>
          <ul>
            {searchOrNodes}
          </ul>
        <h4 id="and_res">And Results</h4>
        <hr/>
          <ul>
            {searchAndNodes}
          </ul>
        </div>
      );
  }
});


var SearchItem = React.createClass({
  render: function() {
    return (
      <a id="ss" href={this.props.search_ob.link}>
      <li id="ll">
      <b id="search_name">{this.props.search_ob.name}</b> <p id="cap">{this.props.search_ob.description}</p>
      </li>
      <hr/>
      </a>

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
var query=getParameterByName('q');
var str1 = "/api/search?q=";
var str2 = str1.concat(query);
console.log(str2);
ReactDOM.render(
    <SearchList url = {str2}/>,
    document.getElementById('content')
);