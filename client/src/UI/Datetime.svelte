<script>
    import {onMount} from "svelte";

    export let dateObj

    let date = ''
    let time = ''
    function dateFormat() {
        let formatted = new Date(dateObj).toLocaleString("ru-RU", {
            day: 'numeric',
            month: 'numeric',
            year: 'numeric',
            hour: 'numeric',
            minute: 'numeric',
        })
        let datetime = formatted.split(", ")
        date = datetime[0]
        time = datetime[1]
    }

    $: if (dateObj) dateFormat();
    onMount(dateFormat)
</script>

{date}
{time}