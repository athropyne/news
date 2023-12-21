<script>
    import {PUBLIC_SERVER_URL} from "$env/static/public";
    import {createEventDispatcher} from "svelte";
    import IconDelete from '../images/icons8-удалить.gif'

    export let id_news;
    let dispatch = createEventDispatcher()

    function sendEventDeleted() {
        alert()
        dispatch('is_deleted')
    }
    async function delete_news() {
        let response = await fetch(`${PUBLIC_SERVER_URL}/${id_news}`, {
            method: "DELETE"
        })
        if (response.ok) {
            sendEventDeleted()
        }
    }
</script>

    <img src="{IconDelete}" height="50" width="50" alt="удалить" on:click={delete_news}/>
