$( document ).ready(function() {
  // twitter
  /**
 * ### HOW TO CREATE A VALID ID TO USE: ###
 * Go to www.twitter.com and sign in as normal, go to your settings page.
 * Go to "Widgets" on the left hand side.
 * Create a new widget for what you need eg "user time line" or "search" etc.
 * Feel free to check "exclude replies" if you don't want replies in results.
 * Now go back to settings page, and then go back to widgets page and
 * you should see the widget you just created. Click edit.
 * Look at the URL in your web browser, you will see a long number like this:
 * 586492039799377920
 * Use this as your ID below instead!
 */
  twitterFetcher.fetch({
    "id": '440758654015242240',
    "domId": 'tweets',
    "maxTweets": 5,
    "enableLinks": true,
    "customCallback":handleTweets,
  });
  
  
  function handleTweets(tweets){
    var i=0;
    var j=tweets.length;
    var l="<ul class='carousel-inner'>";
    while(i<j){
      l+="<li class='item' id='tweet"+i+"'>"+tweets[i]+"</li>";
      i++;
    }
    l+="</ul>";
    document.getElementById("tweets").innerHTML=l;
    var n=(j-1);
    
    $( "#tweet0" ).addClass( "active" );
    
    $('.carousel').carousel({
      interval: 10000
    })
  } 
});
