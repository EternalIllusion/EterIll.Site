<template>
    <div class="container">
        <div class="bg">
            <Background />
        </div>

        <div class="content-container" id="WEBSITE_CONTENT_BASE">
            <main class="content-container-vscroll" id="WEBSITE_CONTENT_VSCR">
                <header>
                    <h1>Lorem Ipsum Dolor</h1>
                    <p> THIS PAGE IS CURRENTLY NOT AVAILABLE FOR DARK SCHEME</p>
                    <p>
                        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Culpa, asperiores minima autem
                        accusantium
                        esse quasi. Tenetur alias voluptatibus rem sequi aliquam unde fugiat repellendus hic.
                    </p>
                </header>

                <section>
                    <button type="button" class="_target disp-btn">Hover Me</button>
                </section>

                <section>
                    <h2>Section Heading</h2>
                    <p>
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus
                        vehicula nisi at urna convallis, sit amet malesuada odio volutpat.
                    </p>

                    <h3>Subsection Heading</h3>
                    <p>
                        Curabitur non mi sit amet tortor fermentum tincidunt. Integer aliquet
                        purus id urna egestas, in convallis erat molestie.
                    </p>

                    <h4>Nested Heading</h4>
                    <p>
                        Donec vel eros sit amet lorem lacinia pulvinar. Sed accumsan, felis vel
                        volutpat pretium, orci risus laoreet ipsum, sit amet malesuada urna
                        justo ut lacus.
                    </p>
                </section>

                <section>
                    <button type="button" class="_target disp-btn">Hover Me</button>
                    <button type="button" class="_target disp-btn">Hover Me</button>
                    <button type="button" class="_target disp-btn">Hover Me</button>
                    <button type="button" class="_target disp-btn">Hover Me</button>
                    <button type="button" class="_target disp-btn">Hover Me</button>
                    <button type="button" class="_target disp-btn">Hover Me</button>
                    <button type="button" class="_target disp-btn">Hover Me</button>
                    <button type="button" class="_target disp-btn">Hover Me</button>
                    <button type="button" class="_target disp-btn">Hover Me</button>
                    <button type="button" class="_target disp-btn">Hover Me</button>
                    <button type="button" class="_target disp-btn">Hover Me</button>
                    <button type="button" class="_target disp-btn">Hover Me</button>
                </section>

                <footer>
                    <p>Footer content with lorem ipsum text and a link to <a href="#">another page</a>.</p>
                </footer>
            </main>
        </div>
    </div>
</template>


<style scoped>
:root{
    --scheme-color: #fff;
}

.container {
    display: flex;
    flex-direction: column;

    .bg {
        top: 0;
        height: 44.99011206325vw;
        overflow: hidden;
        z-index: 90;
        position: relative;
    }

    .content-container {
        box-sizing: border-box;
        border-radius: 1rem;
        padding: 0rem 1rem 1rem 1rem;

        background-color: var(--scheme-color,#fff);
        z-index: 100;
    }

    h1,h2,h3,h4,h5,h6 {
        margin-top: 0;
    }
}

.disp-btn {
    height: 4rem;
    min-width: 12rem;
    border-radius: .5rem;
}
</style>

<script lang="ts" setup>
import { ref } from 'vue';
import Background from '../components/background.vue';
const isDarkScheme = ref(false);
console.debug(isDarkScheme)

</script>