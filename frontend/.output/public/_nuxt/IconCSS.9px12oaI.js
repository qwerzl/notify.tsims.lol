import{q as m,u as f,s as I,v as r,x,o as v,c as d,y as _,_ as S}from"./entry.3_CrUwhK.js";const y=m({__name:"IconCSS",props:{name:{type:String,required:!0},size:{type:String,default:""}},setup(u){f(e=>({"561285a0":p.value}));const s=I(),t=u,l=r(()=>{var e,n;return(n=(e=s.nuxtIcon)==null?void 0:e.aliases)!=null&&n[t.name]?s.nuxtIcon.aliases[t.name]:t.name}),c=r(()=>x(l.value)),p=r(()=>{var o,a;const e=(a=(o=s.nuxtIcon)==null?void 0:o.iconifyApiOptions)==null?void 0:a.url;if(e)try{new URL(e)}catch{console.warn("Nuxt IconCSS: Invalid custom Iconify API URL");return}return`url('${e||"https://api.iconify.design"}/${c.value.prefix}/${c.value.name}.svg')`}),i=r(()=>{var n,o,a;if(!t.size&&typeof((n=s.nuxtIcon)==null?void 0:n.size)=="boolean"&&!((o=s.nuxtIcon)!=null&&o.size))return;const e=t.size||((a=s.nuxtIcon)==null?void 0:a.size)||"1em";return String(Number(e))===e?`${e}px`:e});return(e,n)=>(v(),d("span",{style:_({width:i.value,height:i.value})},null,4))}}),C=S(y,[["__scopeId","data-v-6f5112e8"]]);export{C as default};
