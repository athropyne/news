<script>
    import {page} from "$app/stores";
    import {PUBLIC_SERVER_URL} from "$env/static/public";
    import {onMount} from "svelte";
    import NewsBlock from "../../wievs/NewsBlock.svelte";

    let one_news = null
    let getOneNews = async () => {
        let response = await fetch(`${PUBLIC_SERVER_URL}/${$page.params["news"]}`)
        if (response.status === 200) {
            one_news = await response.json()
        }
    }
    onMount(async () => await getOneNews())
</script>
<article>
    {#await one_news}
        <p>loading</p>
    {:then one_news}
        <NewsBlock news="{one_news}"/>
    {/await}
</article>


