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
        fetch("http://127.0.0.1:8000/tasks/is-done/" + id, {
            method: 'PUT'
        })
    }
</script>


<div style="padding:10px"> 
    <div style="display:inline-block">
        <p style="width:20px; display:inline-block"><b>{i+1}.</b></p>
        <p style="display:inline-block"> due: {due_date} | </p>
        {#if is_done==true}
            <span style="text-decoration: line-through;width:285px; display:inline-block">{description}</span>
        {:else}
            <span style="width:285px; display:inline-block">{description}</span>
        {/if} 
    </div>
    <button class="btn btn-outline-success" type="button" on:click={done}>done</button>
    {#if is_done==true}
        <button class="btn btn-outline-warning" type="button" on:click={remove}>archive</button>
    {:else}
        <button class="btn btn-outline-secondary disabled" type="button" on:click={remove}>archive</button>
    {/if}
</div> 