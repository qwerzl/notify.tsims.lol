import { withQuery, getQuery } from "ufo";

export default defineEventHandler((event) => {
  const config = useRuntimeConfig()
  let target = `http://127.0.0.1:8000/${event.context.params!.slug}`;
  if (event.path.includes("?")) {
    const query = getQuery(event.path);
    target = withQuery(target, query);
  }
  return proxyRequest(
    event,
    target,
    // { headers: { "X-API-KEY": config.API_TOKEN },  }
  )
})
