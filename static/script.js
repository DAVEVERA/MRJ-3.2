/* ============================================================
   MRJ3.0 — Mr. Jealousy Interior Intelligence Tool
   Application Logic
   ============================================================ */

'use strict';

// ── CATALOG (mirrors core.py — single source of truth on server,
//    duplicated here so the flyout can render without an extra API call)
const MR_JEALOUSY_CATALOG = {
  'Aluminium Jaloezieën': [
    { name: 'Like RAL9002',      hex: '#E9E5CE', material: 'Aluminium', sampleUrl: '/media/Catalogus/Looks-Like-9002/ALU_0590_Looks-Like-9002_MAT_MRJEALOUSY_TOP_1024x1024_7446caaa-9d15-4069-92d6-3ddf710f0a1d.png' },
    { name: 'Like RAL9010',      hex: '#F7F9EF', material: 'Aluminium', sampleUrl: '/media/Catalogus/Looks-Like-9010/ALU_0159_Looks-Like-9010_SILK-GLOSS_MRJEALOUSY_TOP_SWATCH_1024x1024_0007.png' },
    { name: 'Moody Munt',        hex: '#98FF98', material: 'Aluminium', sampleUrl: '/media/Catalogus/Moody-Munt/ALU_3790_Moody-Munt_MAT_MRJEALOUSY_TOP_SWATCH_1024x1024_fe054c58-b2d6-41b9-8a2f-7e63c97b1fd0.png' },
    { name: 'Naughty Aubergine', hex: '#472C4C', material: 'Aluminium', sampleUrl: '/media/Catalogus/Naughty-Aubergine/ALU_8222_Naughty-Aubergine_v2_SUPER-MAT_MRJEALOUSY_TOP_1024x1024_dfb711a6-8dbb-476f-8ef0-4325ca6aebcb.png' },
    { name: 'Oud Green',         hex: '#8F9779', material: 'Aluminium', sampleUrl: '/media/Catalogus/Oud-Green/ALU_1229_Oud-Green_MAT_MRJEALOUSY_TOP_SWATCH_1024x1024_a069cbc7-0edd-4213-8f5d-12c5e30f30d3.png' },
    { name: 'Peachy Pink',       hex: '#FFDAB9', material: 'Aluminium', sampleUrl: '/media/Catalogus/Peachy-Pink/ALU_8238_Peachy-Pink_SUPER-MAT_MRJEALOUSY_01_MAIN_KOORD_50mm_1500x1500_42be3990-4e2b-4c58-9e77-b4ef67b2c0ea.jpg' },
    { name: 'Poolside Blue',     hex: '#00BFFF', material: 'Aluminium', sampleUrl: '/media/Catalogus/Poolside-Blue/ALU_8234_Poolside-Blue_SUPER-MAT_MRJEALOUSY_TOP_1024x1024_9d9b6b8c-cdae-4863-8614-262eb018bae2.png' },
    { name: 'Purple Grey',       hex: '#6D6875', material: 'Aluminium', sampleUrl: '/media/Catalogus/Purple-Grey/ALU_2095_Purple-Grey_MAT_MRJEALOUSY_TOP_SWATCH_1024x1024_3d1758b0-7075-4576-bd79-ac3d49fde2b8.png' },
    { name: 'Rocky Rood',        hex: '#8B0000', material: 'Aluminium', sampleUrl: '/media/Catalogus/Rocky-Rood/ALU_5699_Rocky-Rood_MAT_MRJEALOUSY_01_MAIN_KOORD_50mm_1500x1500_301069ec-b4ad-439d-a128-36e58307d44f.jpg' },
    { name: 'Rusty Retro',       hex: '#B7410E', material: 'Aluminium', sampleUrl: '/media/Catalogus/Rusty-Retro/ALU_7919_Rusty-Retro_RUST_MRJEALOUSY_TOP_1024x1024_9e8d82c0-35c3-4939-9e2c-9402ec88f281.png' },
    { name: 'Silk Zwart',        hex: '#050505', material: 'Aluminium', sampleUrl: '/media/Catalogus/Silk-Zwart/ALU_9020_Silk-Zwart_SPARKLY_MRJEALOUSY_TOP_1024x1024_4db5d3d8-81a1-4ddb-aa32-fd02f440f111.png' },
    { name: 'Skinny Dip',        hex: '#F4C2C2', material: 'Aluminium', sampleUrl: '/media/Catalogus/Skinny-Dip/ALU_8266_Skinny-Dip_MAT-SPARKLE_MRJEALOUSY_01_MAIN_KOORD_50mm_1500x1500_01215c2e-f6d9-4ce0-8e7d-46753c58dd56.jpg' },
    { name: 'Smokey Grey',       hex: '#708090', material: 'Aluminium', sampleUrl: '/media/Catalogus/Smokey-Grey/ALU_9018_Smokey-Grey_SPARKLE_MRJEALOUSY_TOP_SWATCH_1024x1024-min.png' },
    { name: 'Soft Naakt',        hex: '#E3BC9A', material: 'Aluminium', sampleUrl: '/media/Catalogus/Soft-Naakt/ALU_9015_Soft-Naakt_SUPER-MAT-DUO-A_MRJEALOUSY_TOP_SWATCH_1024x1024_0a7b9406-a0b9-4c21-b048-b78abfa34cb5.png' },
    { name: 'Soft Terra',        hex: '#E2725B', material: 'Aluminium', sampleUrl: '/media/Catalogus/Soft-Terra/ALU_9019_Soft-Terra_SUPER-MAT_MRJEALOUSY_TOP_1024x1024_351183ef-f366-417f-a1a8-4f8f3455466f.png' },
    { name: 'Stevig Taupe',      hex: '#483C32', material: 'Aluminium', sampleUrl: '/media/Catalogus/Stevig-Taupe/ALU_4544_Stevig-Taupe_SILK-GLOSS_MRJEALOUSY_TOP_1024x1024_23f6ce17-f7d1-44ad-9060-6159f30eacff.png' },
    { name: 'Stormy Taupe',      hex: '#5C5552', material: 'Aluminium', sampleUrl: '/media/Catalogus/Stormy-Taupe/ALU_8236_Stormy-Taupe_SUPER-MAT_MRJEALOUSY_TOP_1024x1024_43cec98d-7761-4198-b3a5-397dada8c168.png' },
    { name: 'Twijfel Taupe',     hex: '#876C5E', material: 'Aluminium', sampleUrl: '/media/Catalogus/Twijfel-Taupe/ALU_9014_Twijfel-Taupe_SUPER-MAT_MRJEALOUSY_01_MAIN_KOORD1500x1500_f0c4b72f-cc58-42a3-8613-b0dc4f4bb0ed.jpg' },
    { name: 'Velvet Brown',      hex: '#4B3621', material: 'Aluminium', sampleUrl: '/media/Catalogus/Velvet-Brown/ALU_9017_Velvet-Brown_SPARK_MRJEALOUSY_TOP_1024x1024_28ed1acb-1276-4408-8491-92f664a17086.png' },
    { name: 'Bold Bruin',        hex: '#654321', material: 'Aluminium', sampleUrl: '/media/Catalogus/Bold-Bruin/ALU_4798_Bold-Bruin_SUPER-MAT_MRJEALOUSY_TOP_SWATCH_1024x1024_3209ffaa-c291-4894-936e-1d54df7e1024.png' },
    { name: 'Butter Geel',       hex: '#F3E5AB', material: 'Aluminium', sampleUrl: '/media/Catalogus/Butter-Geel/ALU_4315_Butter-Geel_MAT_MRJEALOUSY_01_MAIN_KOORD_50mm_1500x1500_94998412-3a05-4417-91e6-869499133260.jpg' },
    { name: 'Cherry Pop',        hex: '#D2042D', material: 'Aluminium', sampleUrl: '/media/Catalogus/Cherry-Pop/ALU_8261_Cherry-Pop_VELVET_MRJEALOUSY_01_MAIN_KOORD_50mm_1500x1500_f89ac437-aa33-41fb-a8ac-f6afc3cb4c24.jpg' },
    { name: 'Cool Grey',         hex: '#A9A9A9', material: 'Aluminium', sampleUrl: '/media/Catalogus/Cool-Grey/ALU_9011_Cool-Grey_SUPER-MAT-DUO-A_MRJEALOUSY_TOP_1024x1024_d61f2511-63a8-4f26-b8d7-e1d7f86c24d2.png' },
    { name: 'Cosmic Blauw',      hex: '#000080', material: 'Aluminium', sampleUrl: '/media/Catalogus/Cosmic-Blauw/ALU_8235_Cosmic-Blauw_SUPER-MAT_MRJEALOUSY_TOP_1024x1024_69979c25-1f00-4fd8-a15a-dc55ccd644fd.png' },
    { name: 'Crazy Karamel',     hex: '#C68E17', material: 'Aluminium', sampleUrl: '/media/Catalogus/Crazy-Karamel/ALU_4394_Crazy-Karamel_MAT_MRJEALOUSY_01_MAIN_KOORD_50mm_1500x1500_a95969d2-2c42-472c-b40c-ca98d81772d4.jpg' },
    { name: 'Drop Zwart',        hex: '#1A1A1A', material: 'Aluminium', sampleUrl: '/media/Catalogus/Drop-Zwart/ALU_1861_Drop-Zwart_MAT_MRJEALOUSY_TOP_SWATCH_1024x1024-min.png' },
    { name: 'Fluffy Naakt',      hex: '#F5DEB3', material: 'Aluminium', sampleUrl: '/media/Catalogus/Fluffy-Naakt/ALU_9021_Fluffy-Naakt_SPARKLY_MRJEALOUSY_01_MAIN_KOORD_50mm_1500x1500-UPDATE_beb76d64-3a68-4902-b00f-6cc94c2733c0.jpg' },
    { name: 'Brushed Nikkel',    hex: '#B0C4DE', material: 'Aluminium', sampleUrl: '/media/Catalogus/Geborsteld-Nikkel/ALU_7325_Geborsteld-Nikkel_BRUSHED_MRJEALOUSY_TOP_SWATCH_1024x1024_0007.png' },
    { name: 'Koffie Koper',      hex: '#B87333', material: 'Aluminium', sampleUrl: '/media/Catalogus/Gebrand-Koper/ALU_7380_Gebrand-Koper_BRUSHED_MRJEALOUSY_TOP_SWATCH_1024x1024_00c4f029-31d0-4ff2-8b02-98d4caab6182.png' },
    { name: 'Glitter Gold',      hex: '#FFD700', material: 'Aluminium', sampleUrl: '/media/Catalogus/Glitter-Gold/ALU_7529_Glitter-Gold_SUPER-SPARKLY_MRJEALOUSY_TOP_SWATCH_1024x1024_ac71dcb9-965c-46fc-b26c-30ba3935ca6f.png' },
    { name: 'Goed Grijs',        hex: '#808080', material: 'Aluminium', sampleUrl: '/media/Catalogus/Goed-Grijs/ALU_1510_Goed-Grijs_SUPER-MAT_MRJEALOUSY_01_MAIN_KOORD1500x1500_b61149c4-07dc-4310-a851-16d25587536f.jpg' },
    { name: 'Jet Black',         hex: '#050505', material: 'Aluminium', sampleUrl: '/media/Catalogus/Jet-Black/ALU_8228_Jet-Black_SUPER-MAT_MRJEALOUSY_TOP_1024x1024_3d0b276f-7c04-4038-9bdf-de065e9cfd2c.png' },
    { name: 'Juicy Olive',       hex: '#808000', material: 'Aluminium', sampleUrl: '/media/Catalogus/Juicy-Olive/ALU_8268_Juicy-Olive_MAT-SPARKLE_MRJEALOUSY_01_MAIN_KOORD_50mm_1500x1500_015e04c2-5484-4b90-8751-2118242bbb12.jpg' },
    { name: 'Koel Blue',         hex: '#AEC6CF', material: 'Aluminium', sampleUrl: '/media/Catalogus/Koel-Blue/ALU_0990_Koel-Blue_MAT_MRJEALOUSY_01_MAIN_KOORD_50mm_1500x1500_fbea5a24-82ec-4d5b-8b95-13dcb97c723a.jpg' },
    { name: 'Like RAL9001',      hex: '#FDF4E3', material: 'Aluminium', sampleUrl: '/media/Catalogus/Looks-Like-9001/ALU_4491_Looks-Like-9001_MAT_MRJEALOUSY_TOP_SWATCH_1024x1024_6d667459-0060-451b-811b-0535050e0c76.png' },
    { name: 'Cowboy Koper',      hex: '#8B4513', material: 'Aluminium', sampleUrl: '/media/Catalogus/Cowboy-Koper/ALU_7381_Cowboy-Koper_BRUSHED_MRJEALOUSY_01_MAIN_KOORD_50mm_1500x1500-UPDATE_54e947fe-f03e-48e7-baa3-442c19cdcda4.jpg' },
  ],
  'Houten Jaloezieën': [
    { name: 'Like RAL9016',    hex: '#F0F8FF', material: 'Hout', sampleUrl: '/media/Catalogus/Looks-Like-9016/ALU_0192_Looks-Like-9016_MAT_MRJEALOUSY_TOP_SWATCH_1024x1024_8b8dd131-8457-4478-ac84-26b0703d93dd.png' },
    { name: 'Mister Sandman',  hex: '#C2B280', material: 'Hout', sampleUrl: '/media/Catalogus/SAND/HOUTEN-JALOEZIE_SAND_MRJEALOUSY_TOP_1024x1024_4b523e1b-34c3-4291-8e42-5bf5ebaaaa22.png' },
    { name: 'Misty Bamboo',    hex: '#DCC098', material: 'Hout', sampleUrl: '/media/Catalogus/MISTY-BAMBOO/BAMBOE-JALOEZIE_MISTY-BAMBOO_MRJEALOUSY_01_MAIN_KOORD_1500x1500_e3578a74-154c-46e6-ad81-d433bc92ce21.jpg' },
    { name: 'Oak Mooi',        hex: '#C3A376', material: 'Hout', sampleUrl: '/media/Catalogus/OAKMOOI/HOUTEN-JALOEZIE_OAKMOOI_MRJEALOUSY_KOORD_MAIN_1500x1500_5a1c1a8f-0e00-4144-85f0-994fad991b55.jpg' },
    { name: 'Parel White',     hex: '#F5F5F5', material: 'Hout', sampleUrl: '/media/Catalogus/WHITE/HOUTEN-JALOEZIE_WHITE_MRJEALOUSY_KOORD_MAIN_1500x1500_2d53cdc9-263f-4546-9a33-c66dcc9728e4.jpg' },
    { name: 'Shades of Grey',  hex: '#808080', material: 'Hout', sampleUrl: '/media/Catalogus/GREY/HOUTEN-JALOEZIE_GREY_MRJEALOUSY_TOP_1024x1024_41c102dd-1ad8-4eb8-a3a2-f185d6e5bd62.png' },
    { name: 'Smokey Taupe',    hex: '#9E958C', material: 'Hout', sampleUrl: '/media/Catalogus/SMOKEYTAUPE/BAMBOE-JALOEZIE_SMOKEYTAUPE_MRJEALOUSY_01_MAIN_KOORD_1500x1500_3990fc50-3b7e-4aa4-8a0e-496d729fb416.jpg' },
    { name: 'Teder Taupe',     hex: '#D8CCBB', material: 'Hout', sampleUrl: '/media/Catalogus/TEDERTAUPE/HOUTEN-JALOEZIE_TEDERTAUPE_MRJEALOUSY_KOORD_MAIN_1500x1500_UPDATE0025_5a28e143-4438-4139-8ee8-fe5878ac17c7.jpg' },
    { name: 'Tiki Taupe',      hex: '#A69686', material: 'Hout', sampleUrl: '/media/Catalogus/TIKITAUPE/BAMBOE-JALOEZIE_TIKITAUPE_MRJEALOUSY_01_MAIN_KOORD_1500x1500_fd8a7a0a-5f3f-4032-a715-6d0c2d7057ea.jpg' },
    { name: 'BBQ Black',       hex: '#111111', material: 'Hout', sampleUrl: '/media/Catalogus/BBQ-BLACK/BAMBOE-JALOEZIE_5081_BBQ-BLACK_MRJEALOUSY_01_MAIN_KOORD_1500x1500_UPDATE0025_48eb9015-6d2a-4f1e-bf23-9f3a4e14e3f6.jpg' },
    { name: 'Behoorlijk Black',hex: '#222222', material: 'Hout', sampleUrl: '/media/Catalogus/BLACK/BAMBOE-JALOEZIE_5079_BLACK_MRJEALOUSY_01_MAIN_KOORD1500x1500-2_6929703f-b633-42fa-a265-223eddd8e237.jpg' },
    { name: 'Bonsai Bamboo',   hex: '#6B8E23', material: 'Hout', sampleUrl: '/media/Catalogus/BONZAI/BAMBOE-JALOEZIE_BONZAI_MRJEALOUSY_TOP_1024x1024_d3a38bca-34a8-4844-b1dd-6dc704eb0ce4.png' },
    { name: 'Bourbon Bamboo',  hex: '#654321', material: 'Hout', sampleUrl: '/media/Catalogus/BOURBON/BAMBOE-JALOEZIE_BOURBON_MRJEALOUSY_01_MAIN_KOORD_1500x1500_6ad88844-0811-4346-8f89-71b1dfecd9de.jpg' },
    { name: 'De Naturist',     hex: '#D2B48C', material: 'Hout', sampleUrl: '/media/Catalogus/NATURAL/BAMBOE-JALOEZIE_5072_NATURAL_MRJEALOUSY_TOP_1024x1024_ba7c8107-70d1-43dd-a529-02f4c3b971ab.png' },
    { name: 'Donker Brown',    hex: '#3B2F2F', material: 'Hout', sampleUrl: '/media/Catalogus/DARK-BROWN/BAMBOE-JALOEZIE_5072_DARK-BROWN_MRJEALOUSY_TOP_1024x1024_416f5253-08e5-4168-a8a3-7ff799951240.png' },
    { name: 'Eigenlijk Eiken', hex: '#A0785A', material: 'Hout', sampleUrl: '/media/Catalogus/OAK/BAMBOE-JALOEZIE_5072_OAK_MRJEALOUSY_TOP_1024x1024_d3ca885b-8fea-46a0-9a72-d2c5c7f1c65e.png' },
    { name: 'Flat White',      hex: '#FFFAF0', material: 'Hout', sampleUrl: '/media/Catalogus/WHITE/HOUTEN-JALOEZIE_WHITE_MRJEALOUSY_KOORD_MAIN_1500x1500_2d53cdc9-263f-4546-9a33-c66dcc9728e4.jpg' },
    { name: 'Gebroken White',  hex: '#FDF5E6', material: 'Hout', sampleUrl: '/media/Catalogus/GEBROKEN-WHITE/HOUTEN-JALOEZIE_GEBROKEN-WHITE_MRJEALOUSY_KOORD_MAIN_1500x1500_1f3f4314-50c3-46ed-80ee-9f6e4479f680.jpg' },
    { name: 'Haver Milk',      hex: '#EFEBD8', material: 'Hout', sampleUrl: '/media/Catalogus/HAVERMILK/BAMBOE-JALOEZIE_HAVERMILK_MRJEALOUSY_01_MAIN-SHUT_KOORD_1500x1500_7e2e1ca1-077a-41f3-86d1-ffc0b0f4b46d.jpg' },
    { name: 'Smokey Bamboo',   hex: '#4A4A4A', material: 'Hout', sampleUrl: '/media/Catalogus/SMOKEYTAUPE/BAMBOE-JALOEZIE_SMOKEYTAUPE_MRJEALOUSY_01_MAIN_KOORD_1500x1500_3990fc50-3b7e-4aa4-8a0e-496d729fb416.jpg' },
    { name: 'Deep Zwart',      hex: '#080808', material: 'Hout', sampleUrl: '/media/Catalogus/BBQ-BLACK/BAMBOE-JALOEZIE_5081_BBQ-BLACK_MRJEALOUSY_01_MAIN_KOORD_1500x1500_UPDATE0025_48eb9015-6d2a-4f1e-bf23-9f3a4e14e3f6.jpg' },
  ],
};

// ── APPLICATION STATE ──────────────────────────────────────────

const APP = {
  currentPage: 'landing',   // 'landing' | 'loading' | 'result'
  uploadedImageBase64: null,
  analysisResult: null,
  selectedColor: null,       // { name, hex, material, sampleUrl, productType }
  flyoutMaterial: 'Aluminium Jaloezieën',
  progressInterval: null,
  renderBusy: false,
};

// ── DOM REFS ───────────────────────────────────────────────────

const pages = {
  landing: document.getElementById('page-landing'),
  loading: document.getElementById('page-loading'),
  result:  document.getElementById('page-result'),
};

// ── PAGE NAVIGATION ────────────────────────────────────────────

function showPage(name) {
  Object.values(pages).forEach(p => p.classList.remove('active'));
  pages[name].classList.add('active');
  APP.currentPage = name;
  if (name === 'landing') resetChatSequence();
}

// ── CHAT SEQUENCE (loading page) ───────────────────────────────

function animateChatSequence() {
  setTimeout(() => {
    const el = document.getElementById('cm-1');
    if (el) el.classList.add('visible');
  }, 350);
}

function resetChatSequence() {
  const el = document.getElementById('cm-1');
  if (el) el.classList.remove('visible');
}

// ── PROGRESS BAR ───────────────────────────────────────────────

function startProgress() {
  const fill = document.getElementById('progress-fill');
  fill.style.width = '0%';
  let pct = 0;
  APP.progressInterval = setInterval(() => {
    if (pct < 92) {
      pct += Math.random() * 3.5;
      fill.style.width = Math.min(pct, 92) + '%';
    }
  }, 400);
}

function completeProgress() {
  clearInterval(APP.progressInterval);
  document.getElementById('progress-fill').style.width = '100%';
}

// ── IMAGE UPLOAD ───────────────────────────────────────────────

function fileToBase64(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = e => resolve(e.target.result);
    reader.onerror = reject;
    reader.readAsDataURL(file);
  });
}

async function handleFile(file) {
  if (!file || !file.type.match(/image\/(png|jpeg|webp)/)) {
    alert('Gebruik een PNG, JPG of WEBP afbeelding.');
    return;
  }
  if (file.size > 4 * 1024 * 1024) {
    alert('De afbeelding is te groot. Maximaal 4MB toegestaan.');
    return;
  }

  const base64 = await fileToBase64(file);
  APP.uploadedImageBase64 = base64;

  showPage('loading');
  startProgress();
  animateChatSequence();

  try {
    const result = await analyzeImage(base64);
    completeProgress();
    await sleep(400);
    populateResult(result);
    showPage('result');
  } catch (err) {
    completeProgress();
    await sleep(300);
    showPage('result');
    showError(err.message || 'Er is iets misgegaan. Probeer een andere foto.');
  }
}

// ── API CALLS ──────────────────────────────────────────────────

async function analyzeImage(base64) {
  const resp = await fetch('/analyze', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ image: base64 }),
  });
  if (!resp.ok) {
    const err = await resp.json().catch(() => ({}));
    throw new Error(err.error || `Server fout: ${resp.status}`);
  }
  return resp.json();
}

async function renderVisualization() {
  if (APP.renderBusy || !APP.uploadedImageBase64 || !APP.selectedColor) return;
  APP.renderBusy = true;

  const btns = document.querySelectorAll('#btn-visualiseer-top, #btn-visualiseer-bottom');
  btns.forEach(b => { b.disabled = true; b.textContent = '⏳ Renderen…'; });

  const config = {
    productType:  APP.selectedColor.productType,
    material:     APP.selectedColor.material,
    colorName:    APP.selectedColor.name,
    colorHex:     APP.selectedColor.hex,
  };

  const extraOptions = {
    lighting:   getSelected('rg-dagdeel'),
    ladderTape: getSelected('rg-ladder') === 'Ladderband',
    slatWidth:  getSelected('rg-lamel'),
  };

  const mounting = APP.analysisResult?.windowCheck?.recommendation || 'in de dag';
  const state    = getSelected('rg-kantel') === 'Open' ? 'Tot de helft' : 'Geheel uitgerold';

  try {
    const resp = await fetch('/render', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        image:    APP.uploadedImageBase64,
        config,
        mounting,
        state,
        extraOptions,
        analysis: APP.analysisResult,
      }),
    });
    if (!resp.ok) throw new Error(`Render fout: ${resp.status}`);
    const data = await resp.json();
    if (data.image) {
      document.getElementById('ba-after').src = data.image;
      setSliderPosition(50);
    }
  } catch (err) {
    alert('Visualisatie mislukt: ' + err.message);
  } finally {
    APP.renderBusy = false;
    btns.forEach(b => { b.disabled = false; b.textContent = '✨ Resultaat visualiseren'; });
  }
}

// ── POPULATE RESULT ────────────────────────────────────────────

function populateResult(result) {
  APP.analysisResult = result;
  hideError();

  // Before image
  document.getElementById('ba-before').src = APP.uploadedImageBase64;
  document.getElementById('ba-after').src  = APP.uploadedImageBase64;

  // Quality check gate
  if (result.qualityFailed) {
    showError(result.qualityFeedback || 'De foto voldoet niet aan de kwaliteitseisen.');
    return;
  }

  // Suggestions (top 3)
  const suggestions = (result.suggestions || []).slice(0, 3);
  renderSuggestions(suggestions);

  // Select first suggestion as default
  if (suggestions.length > 0) {
    selectColor({
      ...findCatalogColor(suggestions[0].colorName, suggestions[0].productType),
      productType: suggestions[0].productType,
    });
  }

  // Technical check
  const wc = result.windowCheck || {};
  document.getElementById('tc-type').textContent     = wc.windowType    || '—';
  document.getElementById('tc-plaatsing').textContent = wc.recommendation || '—';
  document.getElementById('tc-aantal').textContent   = wc.detectedWindowCount ?? '—';

  // Special considerations
  document.getElementById('special-text').textContent =
    wc.specialConsiderations || wc.reasoning || '—';

  // Style description
  document.getElementById('style-description').textContent =
    result.styleDescription || '';

  // Reset slider
  setSliderPosition(50);
}

function renderSuggestions(suggestions) {
  const list = document.getElementById('suggestion-list');
  list.innerHTML = '';

  suggestions.forEach((s, i) => {
    const color = findCatalogColor(s.colorName, s.productType) || {
      name: s.colorName, material: s.material || s.productType, sampleUrl: '', hex: s.colorHex,
    };
    const card = document.createElement('div');
    card.className = 'suggestion-card' + (i === 0 ? ' selected' : '');
    card.dataset.index = i;
    card.innerHTML = `
      <img class="suggestion-thumb"
           src="${escHtml(color.sampleUrl)}"
           alt="${escHtml(color.name)}"
           onerror="this.style.background='#e0d0c8'"
      />
      <div class="suggestion-info">
        <div class="suggestion-name">${escHtml(color.name)}</div>
        <div class="suggestion-material">${escHtml(color.material)}</div>
      </div>
      <svg class="suggestion-chevron" viewBox="0 0 24 24" fill="none">
        <polyline points="6 9 12 15 18 9" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    `;
    card.addEventListener('click', () => {
      document.querySelectorAll('.suggestion-card').forEach(c => c.classList.remove('selected'));
      card.classList.add('selected');
      selectColor({ ...color, productType: s.productType });
    });
    list.appendChild(card);
  });
}

function selectColor(color) {
  APP.selectedColor = color;
  document.getElementById('color-hero-img').src         = color.sampleUrl || '';
  document.getElementById('color-hero-name').textContent = color.name     || '—';
  document.getElementById('color-hero-material').textContent = color.material || '—';
}

function findCatalogColor(name, productType) {
  const list = productType ? MR_JEALOUSY_CATALOG[productType] : null;
  if (list) {
    const found = list.find(c => c.name === name);
    if (found) return found;
  }
  // Fallback: search all
  for (const [pt, colors] of Object.entries(MR_JEALOUSY_CATALOG)) {
    const found = colors.find(c => c.name === name);
    if (found) return { ...found, productType: pt };
  }
  return null;
}

// ── ERROR DISPLAY ──────────────────────────────────────────────

function showError(msg) {
  const banner = document.getElementById('error-banner');
  banner.textContent = msg;
  banner.classList.add('visible');
}

function hideError() {
  document.getElementById('error-banner').classList.remove('visible');
}

// ── BEFORE / AFTER SLIDER ──────────────────────────────────────

let isDraggingSlider = false;

function setSliderPosition(pct) {
  const divider = document.getElementById('ba-divider');
  const handle  = document.getElementById('ba-handle');
  const after   = document.getElementById('ba-after');
  const clipped = Math.max(0, Math.min(100, pct));
  divider.style.left   = clipped + '%';
  handle.style.left    = clipped + '%';
  after.style.clipPath = `inset(0 ${100 - clipped}% 0 0)`;
}

function initSlider() {
  const container = document.getElementById('ba-container');

  function getPos(e) {
    const rect = container.getBoundingClientRect();
    const clientX = e.touches ? e.touches[0].clientX : e.clientX;
    return ((clientX - rect.left) / rect.width) * 100;
  }

  container.addEventListener('mousedown', e => {
    isDraggingSlider = true;
    setSliderPosition(getPos(e));
    e.preventDefault();
  });

  container.addEventListener('touchstart', e => {
    isDraggingSlider = true;
    setSliderPosition(getPos(e));
  }, { passive: true });

  window.addEventListener('mousemove', e => {
    if (isDraggingSlider) setSliderPosition(getPos(e));
  });

  window.addEventListener('touchmove', e => {
    if (isDraggingSlider) setSliderPosition(getPos(e));
  }, { passive: true });

  window.addEventListener('mouseup',   () => { isDraggingSlider = false; });
  window.addEventListener('touchend',  () => { isDraggingSlider = false; });
}

// ── RADIO GROUPS ───────────────────────────────────────────────

function initRadioGroup(groupId) {
  const group = document.getElementById(groupId);
  if (!group) return;
  group.querySelectorAll('.radio-item').forEach(item => {
    item.addEventListener('click', () => {
      group.querySelectorAll('.radio-item').forEach(i => i.classList.remove('selected'));
      item.classList.add('selected');
    });
  });
}

function getSelected(groupId) {
  const group = document.getElementById(groupId);
  if (!group) return null;
  const selected = group.querySelector('.radio-item.selected');
  return selected ? selected.dataset.value : null;
}

// ── FLYOUT ─────────────────────────────────────────────────────

function openFlyout() {
  const overlay = document.getElementById('flyout-overlay');
  overlay.classList.add('open');
  renderFlyoutList();
}

function closeFlyout() {
  document.getElementById('flyout-overlay').classList.remove('open');
}

function renderFlyoutList() {
  const list    = document.getElementById('flyout-list');
  const colors  = MR_JEALOUSY_CATALOG[APP.flyoutMaterial] || [];
  list.innerHTML = '';

  colors.forEach(color => {
    const item = document.createElement('div');
    const isSelected = APP.selectedColor && APP.selectedColor.name === color.name;
    item.className = 'flyout-item' + (isSelected ? ' selected' : '');
    item.innerHTML = `
      <img class="flyout-thumb"
           src="${escHtml(color.sampleUrl)}"
           alt="${escHtml(color.name)}"
           onerror="this.style.background='#e0d0c8'"
      />
      <div>
        <div class="flyout-name">${escHtml(color.name)}</div>
        <div class="flyout-material">${escHtml(color.material)}</div>
      </div>
    `;
    item.addEventListener('click', () => {
      selectColor({ ...color, productType: APP.flyoutMaterial });
      closeFlyout();
      // Also update suggestion cards to deselect
      document.querySelectorAll('.suggestion-card').forEach(c => c.classList.remove('selected'));
    });
    list.appendChild(item);
  });
}

function initFlyoutMaterialToggle() {
  const toggle = document.getElementById('mat-toggle');
  toggle.querySelectorAll('.radio-item').forEach(item => {
    item.addEventListener('click', () => {
      toggle.querySelectorAll('.radio-item').forEach(i => i.classList.remove('selected'));
      item.classList.add('selected');
      APP.flyoutMaterial = item.dataset.value;
      renderFlyoutList();
    });
  });
}

// ── DRAG & DROP ON UPLOAD ZONE ─────────────────────────────────

function initUploadZone() {
  const zone  = document.getElementById('upload-zone');
  const input = document.getElementById('file-input');

  input.addEventListener('change', e => {
    if (e.target.files[0]) handleFile(e.target.files[0]);
  });

  zone.addEventListener('dragover', e => {
    e.preventDefault();
    zone.classList.add('drag-over');
  });

  zone.addEventListener('dragleave', () => zone.classList.remove('drag-over'));

  zone.addEventListener('drop', e => {
    e.preventDefault();
    zone.classList.remove('drag-over');
    const file = e.dataTransfer.files[0];
    if (file) handleFile(file);
  });
}

// ── SAVE / DOWNLOAD ────────────────────────────────────────────

function saveResult() {
  const afterSrc = document.getElementById('ba-after').src;
  if (!afterSrc || afterSrc === APP.uploadedImageBase64) return;
  const a = document.createElement('a');
  a.href     = afterSrc;
  a.download = 'mr-jealousy-visualisatie.jpg';
  a.click();
}

// ── UTILITY ────────────────────────────────────────────────────

function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

function escHtml(str) {
  if (!str) return '';
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

// ── INIT ───────────────────────────────────────────────────────

document.addEventListener('DOMContentLoaded', () => {

  // Upload zone
  initUploadZone();

  // Slider
  initSlider();

  // Radio groups
  ['rg-ladder', 'rg-lamel', 'rg-kantel', 'rg-dagdeel'].forEach(initRadioGroup);

  // Flyout material toggle
  initFlyoutMaterialToggle();

  // Close buttons → back to landing
  // Always reset the file input so the same file can be re-uploaded.
  function goToLanding() {
    document.getElementById('file-input').value = '';
    showPage('landing');
  }

  document.getElementById('btn-sluiten-landing').addEventListener('click',
    () => window.location.reload());
  document.getElementById('btn-afsluiten-loading').addEventListener('click',
    () => { clearInterval(APP.progressInterval); goToLanding(); });
  document.getElementById('btn-afsluiten-result').addEventListener('click', goToLanding);

  // Kleuren flyout
  document.getElementById('btn-kleuren').addEventListener('click', openFlyout);
  document.getElementById('btn-flyout-sluiten').addEventListener('click', closeFlyout);
  document.getElementById('flyout-overlay').addEventListener('click', e => {
    if (e.target === document.getElementById('flyout-overlay')) closeFlyout();
  });

  // Visualiseer buttons
  document.getElementById('btn-visualiseer-top').addEventListener('click', renderVisualization);
  document.getElementById('btn-visualiseer-bottom').addEventListener('click', renderVisualization);

  // Opnieuw & Opslaan
  document.getElementById('btn-opnieuw').addEventListener('click', goToLanding);
  document.getElementById('btn-opslaan').addEventListener('click', saveResult);

  // Keyboard: Escape closes flyout
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') closeFlyout();
  });

  // Initialize slider at center
  setSliderPosition(50);
});
