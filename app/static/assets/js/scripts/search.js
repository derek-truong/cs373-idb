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
    this.loadDataFromServer();
  },
  render: function() {
    if (isEmptyObject(this.state.data['or_results']) || isEmptyObject(this.state.data['and_results'])) {
      return (<p>Nothing found</p>);
    } else {
      var searchOrNodes = this.state.data['or_results'].map(function(search) {
        return (<SearchItem search_ob={search}/>);});

      var searchAndNodes = this.state.data['and_results'].map(function(search) {
        return (<SearchItem search_ob={search}/>);});
      
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
    return (null);
  }
});
var SearchItem = React.createClass({
  render: function() {
    var name = this.props.search_ob.name;
    var regex = new RegExp("("+getParameterByName('q')+")","gi");
    var line = name.split(regex);
    var output = []

    for(var i=0; i<line.length;i++){
      if(line[i] != undefined && line[i].search(regex)===0)
        output.push(<span id="result">{line[i]}</span>);
      else
        output.push(line[i])
    }

    var description = this.props.search_ob.description;
    var line2 = description.split(regex);
    var output2 = []

    for(var i=0; i<line2.length;i++){
      if(line2[i] != undefined && line2[i].search(regex)===0)
        output2.push(<span id="result">{line2[i]}</span>);
      else
        output2.push(line2[i])
    }

    var address = this.props.search_ob.address;
    var line3= address.split(regex);
    var output3 = []

    for(var i=0; i<line3.length;i++){
      if(line3[i] != undefined && line3[i].search(regex)===0)
        output3.push(<span id="result">{line3[i]}</span>);
      else
        output3.push(line3[i])
    }

    return (
      <a id="ss" href={this.props.search_ob.link}>
      <li id="ll">
        <p id="search_name">{output}</p> 
        <p className="cap">{output2}<br/>{output3}</p>
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