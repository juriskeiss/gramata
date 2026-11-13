--[[
  LRAL mācību grāmatas Pandoc filtrs.

  Pārveido VEIDNE.md pierakstu par maketa blokiem:
    - nodaļas virsrakstu, ievadteikumu, meta rindas un mācību mērķus
      par nodaļas atvēruma lapu;
    - izceltos lodziņus (Praktisks padoms., Uzmanību!, Piemērs., Atceries:,
      Padziļināti.) par krāsainām kartītēm;
    - numurētus apakšvirsrakstus (5.1. ...) par virsrakstu ar uzrakstu;
    - nodaļas beigu sadaļas (Eksāmenā jāzina, Pamēģini pats, Kopsavilkums,
      Paškontroles jautājumi, Atbildes, Padziļināti, Nodaļas avoti) par
      atsevišķiem blokiem;
    - testa jautājumu atbilžu variantus par burtu nozīmītēm;
    - neesošu attēlu par vietturi ar faila nosaukumu.

  Ikonas, krāsas un izkārtojums ir gramata.css; nodaļas ikonas un uzrakstus
  pievieno makets.py.
]]

local stringify = pandoc.utils.stringify

local CALLOUTS = {
  ["Praktisks padoms."] = { cls = "padoms",   label = "Praktisks padoms" },
  ["Uzmanību!"]         = { cls = "uzmanibu", label = "Uzmanību!" },
  ["Piemērs."]          = { cls = "piemers",  label = "Piemērs" },
  ["Atceries:"]         = { cls = "atceries", label = "Atceries" },
  ["Padziļināti."]      = { cls = "padzilinati", label = "Padziļināti" },
}

local SECTIONS = {
  ["Pēc šīs nodaļas tu pratīsi"] = { cls = "merki" },
  ["Eksāmenā jāzina"]           = { cls = "jazina" },
  ["Pamēģini pats"]             = { cls = "pameigini", kicker = "Praktiski" },
  ["Kopsavilkums"]              = { cls = "kopsavilkums", kicker = "Atkārto" },
  ["Paškontroles jautājumi"]    = { cls = "jautajumi", kicker = "Paškontrole" },
  ["Atbildes"]                  = { cls = "atbildes",  kicker = "Paškontrole" },
  ["Padziļināti"]               = { cls = "padzilinati-sad", kicker = "Neobligāti" },
  ["Nodaļas avoti"]             = { cls = "avoti",     kicker = "Avoti" },
}

local function esc(s)
  return (s:gsub("&", "&amp;"):gsub("<", "&lt;"):gsub(">", "&gt;"):gsub('"', "&quot;"))
end

local function html(blocks)
  return pandoc.write(pandoc.Pandoc(blocks), "html5", { html_math_method = "mathml" })
end

local function inline_html(inlines)
  local s = html({ pandoc.Plain(inlines) })
  return s
end

-- ---------------------------------------------------------------- lodziņi
local function callout(bq)
  local first = bq.content[1]
  if not first or (first.t ~= "Para" and first.t ~= "Plain") then return nil end
  local lead = first.content[1]
  if not lead or lead.t ~= "Strong" then return nil end
  local key = stringify(lead)
  local spec = CALLOUTS[key]
  if not spec then return nil end
  -- noņem nosaukumu un sekojošo atstarpi no pirmās rindkopas
  local rest = pandoc.List()
  for i = 2, #first.content do rest:insert(first.content[i]) end
  while #rest > 0 and (rest[1].t == "Space" or rest[1].t == "SoftBreak") do rest:remove(1) end
  local body = pandoc.List()
  if #rest > 0 then body:insert(pandoc.Para(rest)) end
  for i = 2, #bq.content do body:insert(bq.content[i]) end
  local label = pandoc.Div(
    { pandoc.Plain({ pandoc.RawInline("html", '<span class="ikona"></span>'), pandoc.Str(spec.label) }) },
    pandoc.Attr("", { "lodzins-nosaukums" }))
  local content = pandoc.List({ label })
  content:extend(body)
  return pandoc.Div(content, pandoc.Attr("", { "lodzins", spec.cls }))
end

-- ------------------------------------------------------------- attēli
local function figure_fix(fig)
  -- Pandoc 3: Figure ar Image iekšā
  local img
  fig:walk({ Image = function(i) img = i end })
  if not img then return nil end
  local src = img.src
  local f = io.open(src, "r")
  local caption = stringify(fig.caption.long or {})
  if caption == "" then caption = stringify(img.caption) end
  local num, rest = caption:match("^(%d+%.%d+%.%s*attēls%.)%s*(.*)$")
  local cap_html
  if num then
    cap_html = '<span class="att-nr">' .. esc(num) .. '</span> ' .. esc(rest)
  else
    cap_html = esc(caption)
  end
  local inner
  if f then
    f:close()
    local abs = pandoc.path.normalize(pandoc.path.join({ pandoc.system.get_working_directory(), src }))
    inner = '<img src="file://' .. esc(abs) .. '" alt="' .. esc(caption) .. '">'
  else
    inner = '<div class="att-vietturis"><span>Zīmējums</span><code>' ..
            esc(pandoc.path.filename(src)) .. '</code></div>'
  end
  return pandoc.RawBlock("html",
    '<figure class="attels"><div class="att-ramis">' .. inner ..
    '</div><figcaption>' .. cap_html .. '</figcaption></figure>')
end

-- ------------------------------------------------- testa jautājumi
local function quiz_list(ol)
  local items = pandoc.List()
  for _, item in ipairs(ol.content) do
    local new = pandoc.List()
    local short = true
    for _, b in ipairs(item) do
      if b.t == "BulletList" then
        local opts = pandoc.List()
        for _, opt in ipairs(b.content) do
          local txt = stringify(opt)
          local letter, body = txt:match("^([A-D])%.%s*(.*)$")
          if letter then
            if #body > 34 then short = false end
            opts:insert('<li><span class="burts">' .. letter .. '</span><span>' ..
                        esc(body) .. '</span></li>')
          else
            short = false
            opts:insert('<li>' .. html(opt) .. '</li>')
          end
        end
        new:insert(pandoc.RawBlock("html",
          '<ul class="varianti' .. (short and " divas-kolonnas" or "") .. '">' ..
          table.concat(opts, "") .. '</ul>'))
      else
        new:insert(b)
      end
    end
    items:insert(new)
  end
  ol.content = items
  local st = (ol.start or 1) > 1 and { style = "counter-reset: jaut " .. (ol.start - 1) } or {}
  return pandoc.Div({ ol }, pandoc.Attr("", { "jautajumu-saraksts" }, st))
end

-- -------------------------------------------------------- dokuments
function Pandoc(doc)
  local blocks = doc.blocks
  local out = pandoc.List()
  local chapter = { num = "", title = "", lead = "", meta = {}, goals = nil }

  -- 1. solis: atrod nodaļas virsrakstu, ievadu, meta rindas un mērķus
  local i = 1
  local body_start = 1
  if blocks[1] and blocks[1].t == "Header" and blocks[1].level == 1 then
    local h = stringify(blocks[1])
    local n, t = h:match("^(%d+)%.%s*nodaļa%.%s*(.*)$")
    chapter.num = n or ""
    chapter.title = t or h
    i = 2
    if blocks[i] and blocks[i].t == "Para" and not stringify(blocks[i]):match("^Video lekcija") then
      chapter.lead = inline_html(blocks[i].content)
      i = i + 1
    end
    if blocks[i] and blocks[i].t == "Para" and stringify(blocks[i]):match("Video lekcija") then
      -- sadala pa rindām (SoftBreak / LineBreak)
      local line = pandoc.List()
      local lines = {}
      for _, el in ipairs(blocks[i].content) do
        if el.t == "SoftBreak" or el.t == "LineBreak" then
          table.insert(lines, line); line = pandoc.List()
        else line:insert(el) end
      end
      table.insert(lines, line)
      for _, l in ipairs(lines) do
        local key = stringify(l[1] or "")
        local rest = pandoc.List()
        for k = 2, #l do rest:insert(l[k]) end
        while #rest > 0 and rest[1].t == "Space" do rest:remove(1) end
        local val = stringify(rest)
        val = val:gsub("%s*%(QR kod[si]%)", "")
        table.insert(chapter.meta, { key = key:gsub(":$", ""), val = val })
      end
      i = i + 1
    end
    if blocks[i] and blocks[i].t == "Header" and stringify(blocks[i]) == "Pēc šīs nodaļas tu pratīsi" then
      if blocks[i + 1] and blocks[i + 1].t == "BulletList" then
        chapter.goals = blocks[i + 1]
        i = i + 2
      else
        i = i + 1
      end
    end
    body_start = i
  end

  -- atvēruma dati makets.py lietošanai (JSON komentārā)
  local meta_items = {}
  for _, m in ipairs(chapter.meta) do
    table.insert(meta_items, '<div class="meta-rinda"><dt>' .. esc(m.key) ..
      '</dt><dd>' .. esc(m.val) .. '</dd></div>')
  end
  local goals_html = ""
  if chapter.goals then
    local lis = {}
    for _, it in ipairs(chapter.goals.content) do
      table.insert(lis, '<li>' .. html({ pandoc.Plain(it[1].content) }) .. '</li>')
    end
    goals_html = '<ol class="merki-saraksts">' .. table.concat(lis, "") .. '</ol>'
  end
  if chapter.num ~= "" then
    out:insert(pandoc.RawBlock("html",
      '<!--NODALA-ATVERUMS ' .. chapter.num .. '-->' ..
      '<template class="atv-dati" data-num="' .. chapter.num .. '" data-title="' .. esc(chapter.title) .. '">' ..
      '<div class="atv-ievads">' .. chapter.lead .. '</div>' ..
      '<dl class="atv-meta">' .. table.concat(meta_items, "") .. '</dl>' ..
      goals_html .. '</template>'))
  end

  -- 2. solis: pamatteksts ar sadaļu blokiem
  local section = nil      -- pašreizējais īpašais bloks
  local function flush()
    if section then out:insert(section); section = nil end
  end
  for k = body_start, #blocks do
    local b = blocks[k]
    if b.t == "Header" and b.level == 2 then
      flush()
      local text = stringify(b)
      local spec = SECTIONS[text]
      local ckat = b.classes:includes("c-kategorija")
      local ctag = ckat and '<span class="c-kat">Arī C kategorijai</span>' or ""
      if spec then
        local kick = spec.kicker and ('<span class="kicker">' .. esc(spec.kicker) .. '</span>') or ""
        section = pandoc.Div({ pandoc.RawBlock("html",
          '<h2 class="sad-virsraksts" id="' .. esc(b.identifier) .. '">' .. kick ..
          '<span class="v-teksts">' .. esc(text) .. '</span>' .. ctag .. '</h2>') },
          pandoc.Attr("", { "sadala", spec.cls }))
      else
        local num, title = text:match("^(%d+%.%d+%.)%s*(.*)$")
        if num then
          out:insert(pandoc.RawBlock("html",
            '<h2 id="' .. esc(b.identifier) .. '"><span class="kicker">' .. esc(num) ..
            '</span><span class="v-teksts">' .. inline_html(b.content):gsub("^" .. num:gsub("%.", "%%.") .. "%s*", "") ..
            '</span>' .. ctag .. '</h2>'))
        else
          out:insert(pandoc.RawBlock("html",
            '<h2 id="' .. esc(b.identifier) .. '"><span class="v-teksts">' ..
            inline_html(b.content) .. '</span>' .. ctag .. '</h2>'))
        end
      end
    else
      local nb = b
      if b.t == "BlockQuote" then nb = callout(b) or b end
      if b.t == "Figure" then nb = figure_fix(b) or b end
      if section and section.classes:includes("jautajumi") and b.t == "OrderedList" then
        nb = quiz_list(b)
      end
      if section then section.content:insert(nb) else out:insert(nb) end
    end
  end
  flush()

  doc.blocks = out
  return doc
end
