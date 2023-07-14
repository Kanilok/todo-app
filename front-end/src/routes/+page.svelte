<script>
    /** @type {import('./$types').Actions} */
    export const actions = {
        newtask: async (event) => {
            // TODO log the user in
        }
    };


    /** @type {import('./$types').PageData} */
    export let data;
    let tasks = [];
    for(let i in data.item){
        tasks.push({id: data.item[i].id, description: data.item[i].description, is_done: data.item[i].is_done})
    }

    import Tasks from "./Tasks.svelte";
</script>

<Tasks {tasks}/>

