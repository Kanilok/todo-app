<script>
    import { createEventDispatcher } from "svelte";

    let description = ""
    let date

    const dispatch = createEventDispatcher();

    function onSubmit(){
        dispatch("onSubmit", {description:description, date:date})
    }
</script>

<form on:submit|preventDefault={onSubmit}>
    <div style="margin:8px">
        <input  bind:value={description} type="text" class="form-control" placeholder="Task description..." style="width:250px; display:inline-block">
        <input bind:value={date} type="date" class="form-control" style="width:180px; display:inline-block">
        <button class="btn btn-outline-secondary" action="submit">add new task</button>
    </div>
</form>

<style>
    
</style>
