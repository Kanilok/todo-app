<script>
    /** @type {import('./$types').PageData} */
    export let data;
    let tasks = [];
    for(let i in data.item){
        tasks.push({id: data.item[i].id, 
                    description: data.item[i].description,
                    is_done: data.item[i].is_done,
                    due_date: data.item[i].due_date,
                    add_date: data.item[i].add_date.substring(0,10),
                    done_date: data.item[i].done_date
                })
    }

    import Tasks from "./Tasks.svelte";
</script>

<Tasks {tasks}/>

