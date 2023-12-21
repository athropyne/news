<script>
    import TitleBlock from "../UI/TitleBlock.svelte";
    import Datetime from "../UI/Datetime.svelte";

    export let news = {}
</script>
<a href="/{news['идентификатор']}">
    <div class="news-container">
        <div class="datetime"><Datetime dateObj="{news['дата создания']}"/></div>
        <h3><TitleBlock text="{news['заголовок']}"/></h3>
    </div>
</a>
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
        -moz-box-shadow: -6px 3px 13px  rgba(71, 104, 111, 0.37);
        box-shadow: -6px 3px 3px  rgba(71, 104, 111, 0.37);
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
    .datetime {
        margin: 2px 5px;
        text-align: left;
    }
    a {
        text-decoration: none;
    }

    h3 {
        margin-left: 1em;
        margin-top: 3px;
    }


</style>
