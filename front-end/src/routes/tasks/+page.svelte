<script>
    import { onMount } from 'svelte';
    export let data;
    import Tasks from "./Tasks.svelte";

    let is_fetched = false
    var tasks = [];

    async function fetchDataWithToken(token) {
        try {
        const response = await fetch('http://127.0.0.1:8000/tasks', {
            headers: {
            Authorization: `Bearer ${token}`,
            },
        });
        const data = await response.json();
        for(let i in data){
        tasks.push({id: data[i].id, 
                    description: data[1].description,
                    is_done: data[i].is_done,
                    due_date: data[i].due_date,
                    add_date: data[i].add_date.substring(0,10),
                    done_date: data[i].done_date
                })
        
        }
        console.log(tasks)
        is_fetched = true
        } catch (error) {
        console.error('Error fetching data:', error);
        }
    }

    onMount(() => {
        const token = localStorage.getItem("access_token")

        fetchDataWithToken(token);
    });
    
    /** @type {import('./$types').PageData} */
    // var tasks = [];
    // for(let i in data.item){
    //     tasks.push({id: data.item[i].id, 
    //                 description: data.item[i].description,
    //                 is_done: data.item[i].is_done,
    //                 due_date: data.item[i].due_date,
    //                 add_date: data.item[i].add_date.substring(0,10),
    //                 done_date: data.item[i].done_date
    //             })
    // }
    // console.log(localStorage.getItem("asdf"))
    

    
</script>

{#if is_fetched}
    <Tasks {tasks}/>
{/if}
