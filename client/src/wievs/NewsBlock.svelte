<script>
    import TitleBlock from "../UI/TitleBlock.svelte";
    import Datetime from "../UI/Datetime.svelte";
    import ContentBlock from "../UI/ContentBlock.svelte";
    import DeleteButton from "../UI/DeleteButton.svelte";
    import {goto} from "$app/navigation";

    export let news
    function returnToList() {
        goto('/')
    }
</script>
{#if news}
    <div class="news-container">

        <DeleteButton id_news="{news['идентификатор']}" on:is_deleted={returnToList} />
        <Datetime dateObj='{news["дата создания"]}'/>
        <h3>
            <TitleBlock text="{news['заголовок']}"/>
        </h3>
        <div>
            <ContentBlock text="{news['содержание']}"/>
        </div>
    </div>
{/if}
<style>
    .news-container {
        margin: auto;
        background: aqua;
        border: gold 1px solid;
        border-radius: 8px;
        width: 20em;
        word-wrap: normal;
        padding: 5px;
        text-align: left;
        -webkit-box-shadow: -6px 3px 13px rgba(71, 104, 111, 0.37);
        -moz-box-shadow: -6px 3px 13px rgba(71, 104, 111, 0.37);
        box-shadow: -6px 3px 3px rgba(71, 104, 111, 0.37);
    }

    .news-container:active {
        -webkit-box-shadow: none;
        -moz-box-shadow: none;
        box-shadow: none;
        background: #77ffff;
    }

    .news-container:hover {
        background: #dcdbd4;
    }



    h3 {
        margin-left: 1em;
        margin-top: 3px;
    }


</style>
