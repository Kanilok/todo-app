<script>
    import { createEventDispatcher } from "svelte";

    export let description;
    export let is_done;
    export let id;
    export let i;


    const dispatch = createEventDispatcher();

    function remove(){
        dispatch("remove", id)
    }

    function done(){
        is_done = !is_done;
        fetch("http://127.0.0.1:8000/task/" + id, {
            method: 'PUT'
        })
    }
</script>


<div style="padding:10px"> {i+1}. {#if is_done==true}
    <span style="text-decoration: line-through;width:160px; display:inline-block">{description}</span>
{:else}
    <span style="width:160px; display:inline-block">{description}</span>
{/if} 
<button on:click={done}>done</button>
<button on:click={remove}>delete</button>
</div> 