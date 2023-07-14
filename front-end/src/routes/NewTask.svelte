<script>
    import { createEventDispatcher } from "svelte";

    let description = ""

    const dispatch = createEventDispatcher();

    function onSubmit(){
        dispatch("onSubmit", description)
    }
</script>

<form on:submit|preventDefault={onSubmit}>
    <input bind:value={description} type="text" style="width:178px">
    <button action="submit" style="width:102px">add new task</button>
</form>
