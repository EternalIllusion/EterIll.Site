<template>
  <div class="cursor-container">
    <div class="cursor" :class="{ 'hidden': isFocusing }" id="CUSTOM_CURSOR_CUR_POINTER">
    </div>
    <div class="cursor-focus" id="CUSTOM_CURSOR_CUR_FOCUSING">
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, onMounted, onUnmounted, ref } from 'vue';
import { animate } from 'animejs';

//config area

const transitionTime = 250

const CURSOR_IMAGE_URL = '/pointer_9A239EB457D5E7AF6357366BD62047CB.webp';
const CURSOR_FOCUS_IMAGE_URL = '/focus4x_5AA2020B9F0D94AD3DF67F0D2AB801A7.webp';

const ORIGINAL_HOTSPOT = { x: 1, y: 1 };
const BASE_SIZE = 32;
const BASE_SIZE_FOCUS = 128; // 384/3=128
const BASE_RENDER_SIZE_FOCUS = 32;

const scaleStr = localStorage.getItem('cursor-scale');
const SCALE_MULTIPLIER = scaleStr ? parseFloat(scaleStr) : 1;

const finalSize = BASE_SIZE * SCALE_MULTIPLIER;
const finalFocusSize = BASE_RENDER_SIZE_FOCUS * SCALE_MULTIPLIER;
const currentHotspot = {
  x: ORIGINAL_HOTSPOT.x * SCALE_MULTIPLIER,
  y: ORIGINAL_HOTSPOT.y * SCALE_MULTIPLIER
};

const CURSOR_IMAGE_ATTR = `url(${CURSOR_IMAGE_URL})`;
const CURSOR_SIZE_ATTR = `${finalSize}px`;
const FOCUS_IMAGE_ATTR = `url(${CURSOR_FOCUS_IMAGE_URL})`;
const FOCUS_SIZE_ATTR = `${finalFocusSize}px`;

const isFocusing = ref(false)
const position = reactive({ x: 3276800, y: 3276800 });






const currentTarget = ref<HTMLElement | null>(null);
const lastFocusing = reactive({ x: 3276800, y: 3276800, cx: 3276800, cy: 3276800, w: 0, h: 0 })

const getTargets = (): NodeListOf<HTMLElement> => {
  return document.querySelectorAll('._target');
};

const bindTargetEvents = () => {

  const targets = getTargets();

  targets.forEach((ele) => {
    console.debug(`Binding to ${ele}`)

    ele.addEventListener('mouseenter', (e) => {
      console.debug("->", ele)
      currentTarget.value = ele;
      isFocusing.value = true;
      e.stopPropagation();
      playTransitionAnimation(true);
    });

    ele.addEventListener('mouseleave', (e) => {
      console.debug(`<-`, currentTarget.value)
      currentTarget.value = null;
      isFocusing.value = false;
      e.stopPropagation();
      playTransitionAnimation(false);
    });
    console.debug(`Binding ok!`, ele)
  });
};


const getAnimationArgs = () => {

  let targetX = position.x - currentHotspot.x;
  let targetY = position.y - currentHotspot.y;
  let usingFocus = false;
  let targetXF = -1;
  let targetYF = -1;
  let targetH = -1;
  let targetW = -1;

  if (isFocusing.value && currentTarget.value) {
    const rect = currentTarget.value.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;

    targetXF = rect.left + (position.x - centerX) * 0.1 - BASE_RENDER_SIZE_FOCUS; //snap effect
    targetYF = rect.top + (position.y - centerY) * 0.1 - BASE_RENDER_SIZE_FOCUS;
    usingFocus = true;
    targetH = rect.height;
    targetW = rect.width;
    Object.assign(lastFocusing, { cx: centerX, cy: centerY, w: targetW, h: targetH, x:targetXF, y:targetYF})
  }

  return {
    targetX, targetY,
    usingFocus,
    targetXF, targetYF,
    targetH, targetW
  }
}

const playTransitionAnimation = (enter: boolean = true, instant: boolean = false) => {

  const { targetX, targetY, usingFocus, targetXF, targetYF, targetH, targetW } = getAnimationArgs();

  animate("#CUSTOM_CURSOR_CUR_FOCUSING", {
    translateX: { from: usingFocus ? targetX:lastFocusing.x, to: usingFocus ? targetXF : targetX - lastFocusing.w / 2 },
    translateY: { from: usingFocus ? targetY:lastFocusing.y, to: usingFocus ? targetYF : targetY - lastFocusing.h / 2 },
    opacity: enter ? 1 : 0,
    scale: enter ? 1 : 0,
    duration: instant ? 0 : transitionTime,
    width: { to: usingFocus ? targetW : lastFocusing.w, duration: 0 },
    height: { to: usingFocus ? targetH : lastFocusing.h, duration: 0 },
  })
  animate("#CUSTOM_CURSOR_CUR_POINTER", {
    opacity: enter ? 0 : 1,
    duration: instant ? 0 : transitionTime
  })
}


const handleMouseMove = (e: MouseEvent) => {
  position.x = e.clientX;
  position.y = e.clientY;

  const { targetX, targetY, usingFocus, targetXF, targetYF, targetH, targetW } = getAnimationArgs();

  if (usingFocus) {
    animate("#CUSTOM_CURSOR_CUR_FOCUSING", {
      translateX: targetXF, translateY: targetYF,
      width: targetW, height: targetH,
      duration: 0
    })
  }
  animate("#CUSTOM_CURSOR_CUR_POINTER", { translateX: targetX, translateY: targetY, duration: 0 })

};

onMounted(() => {
  window.addEventListener('mousemove', handleMouseMove);
  bindTargetEvents();
  console.log(`Cursor Scale: ${SCALE_MULTIPLIER}x, Size: ${finalSize}px`);
  playTransitionAnimation(false, true)
});

onUnmounted(() => {
  window.removeEventListener('mousemove', handleMouseMove);

  location.reload();//debug
});

(window as any).setCursorSize = (size: string) => {
  const numSize = parseFloat(size);
  if (isNaN(numSize) || numSize <= 0) {
    console.warn('setCursorSize: Invalid cursor size.');
    return;
  }

  localStorage.setItem('cursor-scale', size);
  location.reload();
};

</script>

<style scoped>
.cursor-container {

  pointer-events: none;
  cursor: none !important;

  display: flex;
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;

}

.cursor {
  position: fixed;
  top: 0;
  left: 0;

  background-image: v-bind(CURSOR_IMAGE_ATTR);
  width: v-bind(CURSOR_SIZE_ATTR);
  height: v-bind(CURSOR_SIZE_ATTR);

  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
  pointer-events: none;
  z-index: 19999;
  image-rendering: pixelated;

  transition: opacity .2s ease-out;

  will-change: transform, opacity;
}

.cursor-focus {
  position: fixed;
  top: 0;
  left: 0;

  border-style: solid;
  border-width: v-bind(FOCUS_SIZE_ATTR);
  border-image-source: v-bind(FOCUS_IMAGE_ATTR);
  border-image-slice: v-bind(BASE_SIZE_FOCUS);
  image-rendering: pixelated;
  z-index: 19999;

  will-change: transform, opacity;
}

.hidden {
  opacity: 0;
}
</style>