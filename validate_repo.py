"""Validate question counts, answer mappings, coverage and local dependencies."""
import collections
import hashlib
import json
import re
from pathlib import Path

course=json.loads(Path('data.json').read_text())
lessons=course['lessons']
questions=[q for l in lessons for q in l['questions']]
assert len(lessons)==8
assert len(questions)==600
assert len({q['id'] for q in questions})==600
assert len({re.sub(r'\W+','',q['question'].casefold()) for q in questions})==600
assert sum(len(l['topics']) for l in lessons)==66
assert sum(len(l['slides']) for l in lessons)==404
for lesson in lessons:
 assert len(lesson['questions'])==75
 topic_ids={t['id'] for t in lesson['topics']}
 for topic in lesson['topics']:
  assert any(q['topicId']==topic['id'] for q in lesson['questions'])
 for q in lesson['questions']:
  assert q['lecture']==lesson['id']
  assert q['topicId'] in topic_ids
  assert len(q['options'])==4
  assert all(isinstance(v,str) and v.strip() for v in q['options'])
  assert len({v.strip().casefold() for v in q['options']})==4
  assert isinstance(q['answer'],int) and 0<=q['answer']<4
  assert q['question'].endswith('?')
  assert len(q['explanation'].split())>=12
  assert q['sourceSlides']
 for slide in lesson['slides']:
  for image in slide.get('images',[]):assert Path(image).is_file(),image
 exported=json.loads(Path(f"question-bank/lecture-{lesson['id']:02}.json").read_text())
 assert exported['questions']==lesson['questions']
assert json.loads(Path('question-bank/600-mcqs.json').read_text())['questions']==questions
for name in ['index.html','style.css','app.js','.nojekyll','COVERAGE.md']:
 assert Path(name).is_file()
assert '80 single-best-answer' not in Path('app.js').read_text()
report={
 'total_questions':600,'questions_per_lecture':{str(l['id']):len(l['questions']) for l in lessons},
 'major_topics_covered':66,'source_slide_sections':404,
 'duplicate_ids':0,'duplicate_stems':0,'missing_topic_mappings':0,
 'invalid_answer_indexes':0,'invalid_option_sets':0,
 'answer_position_counts':dict(collections.Counter('ABCD'[q['answer']] for q in questions)),
 'question_types':dict(collections.Counter(q['difficulty'] for q in questions)),
 'content_sha256':hashlib.sha256(Path('data.json').read_bytes()).hexdigest(),
 'scope':'Structural checks; source-aligned editorial review is separate from automated validation.'}
Path('VALIDATION.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
