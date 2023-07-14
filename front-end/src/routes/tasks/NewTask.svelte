<script>
    import { createEventDispatcher } from "svelte";

    let description = ""

    const dispatch = createEventDispatcher();

    function onSubmit(){
        dispatch("onSubmit", description)
    }
</script>

<form on:submit|preventDefault={onSubmit}>
    <div class="row g-3 align-items-center" style="margin:8px; width:405px">
        <div class="input-group">
            <input  bind:value={description} type="text" class="form-control" placeholder="Task description...">
            <button class="btn btn-outline-secondary" action="submit">add new task</button>
        </div>
    </div>
</form>

<style>
    input:focus{  
        box-shadow: 0 0 6px grey;
        border:grey  
    }
</style>
