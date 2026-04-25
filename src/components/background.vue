<template>
    <div class="_bg_wrapper">
        <div class="_bg_abs_bg"><img :src="BgImg" alt=""></div>
        <div class="_bg_front" id="BACKGROUND_FLOW"><img :src="FgImg" alt=""></div>
        <div class="_bg_interact" id="BACKGROUND_FLOW_INTERACT"></div>
        <div class="covering"></div>
    </div>
</template>

<script setup lang="ts">
import { animate, utils } from 'animejs';
import { onMounted, onUnmounted } from 'vue';

import BgImg from "../assets/flowbg_bg.png";
import FgImg from "../assets/flowbg_front.png";

const AbController = new AbortController()

const onMouseMoving = (e: MouseEvent) => {
    const target = e.currentTarget as HTMLElement;

    const width = target.clientWidth;
    //const height = target.clientHeight;

    const x = e.offsetX;
    //const y = e.offsetY;

    const percentX = x / width;
    //const percentY = y / height;

    animate("#BACKGROUND_FLOW", { translateX: `${percentX*4}%`, duration: 1000 })
    //console.log(`X: ${percentX.toFixed(2)}, Y: ${percentY.toFixed(2)}`);
}

onMounted(() => {
    utils.$("#BACKGROUND_FLOW_INTERACT")[0].addEventListener('mousemove', onMouseMoving as EventListener, { signal: AbController.signal });
})

onUnmounted(() => {
    AbController.abort();
})

</script>

<style scoped>

._bg_wrapper {
    width: 100%;
    max-width: 100vw;
    height: auto;
    position: relative;
    overflow: hidden;
    z-index: 1;

    ._bg_front,
    ._bg_interact {
        position: absolute;
        left: 0;
        right: 0;
        top: 0;
        bottom: 0;
    }

    ._bg_interact {
        z-index: 20001;
    }

    ._bg_front {
        filter: drop-shadow(0 0 1px #000);
    }

    ._bg_abs_bg {
        max-width: 100vw;
        width: 100%;
        opacity: .98;
    }

    img {
        display: block;
        width: 100%;
        height: 100%;
        object-fit: cover;
        margin: 0;
        padding: 0;
    }

    .covering {
        position: absolute;
        top: 100%;
        left: 0;
        right: 0;
        
        height: 2rem;
        border-radius: 1rem;
        background-color: white;

        transform: translateY(-1rem);
        z-index: 20000;
    }

}
</style>