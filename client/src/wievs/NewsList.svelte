<script>
    import {onMount} from "svelte";
    import {PUBLIC_SERVER_URL} from '$env/static/public'
    import NewsPreview from "./NewsPreview.svelte";

    let news_list = []
    let getNews = async () => {
        let response = await fetch(`${PUBLIC_SERVER_URL}/list`)
        let code = response.status
        if (code === 200) {
            let result = await response.json()
            if (result.length > 0) {
                news_list = result
            }
        }
    }
    onMount(async () => await getNews())
</script>
<article>
    {#each news_list as n (n["идентификатор"])}
        <div>
            <NewsPreview news="{n}"/>
        </div>
    {/each}
</article>

<style>
    article {
        text-align: center;
    }

    div {
        margin-bottom: 8px;
    }
</style>
