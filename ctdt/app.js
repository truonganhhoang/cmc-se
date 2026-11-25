(function(){
  var btns=document.querySelectorAll('.filters button'), q=document.getElementById('q'), arts=document.querySelectorAll('article.course'), cnt=document.getElementById('cnt');
  if(!arts.length) return;
  var f='all';
  function apply(){ var s=(q&&q.value||'').toLowerCase().trim(), n=0;
    arts.forEach(function(a){ var ok=(f==='all'||(' '+a.dataset.tags+' ').indexOf(' '+f+' ')>=0)&&(!s||a.textContent.toLowerCase().indexOf(s)>=0); a.classList.toggle('hidden',!ok); if(ok)n++; });
    if(cnt) cnt.textContent=n+' học phần'; }
  btns.forEach(function(b){ b.addEventListener('click',function(){ f=b.dataset.f; btns.forEach(function(x){x.setAttribute('aria-pressed',x===b)}); apply(); }); });
  if(q) q.addEventListener('input',apply);
  apply();
  if(location.hash){ var t=document.getElementById(location.hash.slice(1)); if(t) t.scrollIntoView(); }
})();