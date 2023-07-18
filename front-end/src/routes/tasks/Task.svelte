<script>
    import { createEventDispatcher } from "svelte";

    export let description;
    export let is_done;
    export let id;
    export let due_date;
    export let i;


    const dispatch = createEventDispatcher();

    function remove(){
        dispatch("remove", id)
    }

    function done(){
        is_done = !is_done;
        fetch("http://127.0.0.1:8000/tasks/" + id, {
            method: 'PUT'
        })
    }
</script>


<div style="padding:10px"> 
    <div style="display:inline-block">
        <p style="width:20px; display:inline-block"><b>{i+1}.</b></p>
        <p style="display:inline-block">due: {due_date} |</p>
        {#if is_done==true}
            <span style="text-decoration: line-through;width:220px; display:inline-block">{description}</span>
        {:else}
            <span style="width:220px; display:inline-block">{description}</span>
        {/if} 
    </div>
    <button class="btn btn-outline-success" type="button" on:click={done}>done</button>
    <button class="btn btn-outline-danger" type="button" on:click={remove}>delete</button>
</div> 