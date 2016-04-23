

$(document).ready(function() {
    $('#example').dataTable();

function initMyDataTable() {
 $('#example').dataTable();
   
}
function addTableRow(r){
    $('#example').dataTable().fnAddData(["<a href=\"/restaurants/"+ r.id +"\">"+r.name+"</a>", "<a href=\"/cities/" + r.city_id + "\">" + r.city_name +"</a>", r.rating, r.category.charAt(0).toUpperCase() + r.category.slice(1), r.address]);
}
} );