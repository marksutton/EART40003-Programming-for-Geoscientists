-- Prepare semantic handout structure for the HTML/CSS PDF renderer.
function Pandoc(document)
  local output = pandoc.List()
  local intro = pandoc.List()
  local current_section = nil
  local found_major = false

  for _, block in ipairs(document.blocks) do
    if block.t == "Header" and block.level == 1 then
      found_major = true
      local identifier = block.identifier ~= "" and block.identifier or "section"
      current_section = pandoc.Div(
        pandoc.List({block}),
        pandoc.Attr("", {"major-section", "section-" .. identifier})
      )
      output:insert(current_section)
    elseif current_section ~= nil then
      current_section.content:insert(block)
    elseif not found_major then
      intro:insert(block)
    else
      output:insert(block)
    end
  end

  if #intro > 0 then
    document.meta.handout_intro = pandoc.MetaBlocks(intro)
  end
  document.blocks = output
  return document
end
