<script>
    import {PUBLIC_SERVER_URL} from "$env/static/public";
    import {createEventDispatcher} from "svelte";
    import IconUpdate from '../images/icons8-редактировать.gif'

    export let id_news;
    let dispatch = createEventDispatcher()

    function sendEventDeleted() {
        alert()
        dispatch('is_deleted')
    }
    async function delete_news() {
        let response = await fetch(`${PUBLIC_SERVER_URL}/${id_news}`, {
            method: "PUT"
        })
        if (response.ok) {
            sendEventDeleted()
        }
    }
</script>

<img src="{IconUpdate}" height="50" width="50" alt="удалить" on:click={delete_news}/>
