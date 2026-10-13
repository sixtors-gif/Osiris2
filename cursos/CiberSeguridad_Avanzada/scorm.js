(function(){
function findAPI(w){var tries=0;while(w&&tries<7){try{if(w.API)return w.API;w=w.parent}catch(e){}tries++}return null}
var api=findAPI(window); if(!api) try{api=findAPI(window.opener)}catch(e){}
function call(fn,args){try{if(api&&api[fn])return api[fn].apply(api,args||[])}catch(e){}}
window.scorm={
start:function(){call('LMSInitialize',['']);},
complete:function(score){call('LMSSetValue',['cmi.core.lesson_status','completed']);if(score!=null){call('LMSSetValue',['cmi.core.score.raw',String(score)]);call('LMSSetValue',['cmi.core.score.min','0']);call('LMSSetValue',['cmi.core.score.max','100']);}call('LMSCommit',['']);},
finish:function(){call('LMSFinish',['']);}
}; scorm.start(); window.addEventListener('beforeunload',function(){scorm.finish()});
})();