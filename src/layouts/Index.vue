<template>
    <main>
        <header>
            <h1 class="_target">Lorem Ipsum Dolor</h1>
            <p>
                Lorem ipsum, dolor sit amet consectetur adipisicing elit. Culpa, asperiores minima autem accusantium esse quasi. Tenetur alias voluptatibus rem sequi aliquam unde fugiat repellendus hic.
            </p>
        </header>

        <section>
            <h2 class="_target">Section Heading</h2>
            <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus
                vehicula nisi at urna convallis, sit amet malesuada odio volutpat.
            </p>

            <h3 class="_target">Subsection Heading</h3>
            <p>
                Curabitur non mi sit amet tortor fermentum tincidunt. Integer aliquet
                purus id urna egestas, in convallis erat molestie.
            </p>

            <h4 class="_target">Nested Heading</h4>
            <p>
                Donec vel eros sit amet lorem lacinia pulvinar. Sed accumsan, felis vel
                volutpat pretium, orci risus laoreet ipsum, sit amet malesuada urna
                justo ut lacus.
            </p>
        </section>

        <section>
            <h5 class="_target">Smaller Heading</h5>
            <p>
                <strong>Lorem ipsum dolor</strong> sit amet, <em>consectetur</em>
                adipiscing elit. Phasellus vehicula feugiat massa in hendrerit. Read more
                at
                <a href="https://www.example.com" target="_blank" rel="noopener">
                    example.com
                </a>.
            </p>

            <h6>Smallest Heading</h6>
            <p>
                Aliquam erat volutpat. Maecenas sagittis lacus nec velit aliquet, ac
                vestibulum purus aliquet. Fusce at tortor vitae est tincidunt
                ullamcorper.
            </p>
        </section>

        <section>
            <h2>Lists</h2>
            <p>Ordered list:</p>
            <ol>
                <li>First item ipsum dolor</li>
                <li>Second item sit amet</li>
                <li>Third item consectetur</li>
            </ol>

            <p>Unordered list:</p>
            <ul>
                <li>Vestibulum</li>
                <li>Quisque</li>
                <li>Nullam</li>
            </ul>
        </section>

        <section>
            <h2>Other Elements</h2>
            <blockquote>
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec
                odio. Praesent libero."
            </blockquote>

            <pre><code>const lorem = "ipsum dolor sit amet";</code></pre>

            <button type="button">Click Me</button>
        </section>

        <footer>
            <p>Footer content with lorem ipsum text and a link to <a href="#">another page</a>.</p>
        </footer>
    </main>
</template>


<style scoped>
* {
    width: fit-content;
    border: 1px #88888833 solid;
}
main {
    padding: 3rem;
}
</style>

<script lang="ts" setup>
import { ref } from 'vue'; 
const isDarkScheme = ref(false);
console.debug(isDarkScheme)
</script>