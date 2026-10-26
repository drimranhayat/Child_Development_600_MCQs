"""Append authored questions and attach explicit topic/source metadata."""
import random
from pathlib import Path

BASE_TOPICS={
 1:[1,3,2,6,5,7,7,8,4,8],
 2:[1,4,1,6,7,7,7,7,7,8],
 3:[1,1,3,5,2,7,7,6,8,8],
 4:[6,1,1,3,4,5,6,8,2,7],
 5:[2,2,2,6,8,3,4,4,5,7],
 6:[8,4,5,6,7,6,7,9,8,1],
 7:[1,4,2,2,6,2,8,7,2,1],
 8:[1,7,4,7,5,9,8,1,5,1]
}
def build_bank(lessons):
 stems=set()
 refinements={}
 for row in Path('question-bank/core-option-refinements.txt').read_text().splitlines():
  if row.strip():
   key,*options=row.split('~');assert len(options)==3;refinements[key]=options
 for lesson in lessons:
  number=lesson['id']
  def annotate(question,topic_number):
   if number==2 and "doll's-eye" in question['question']: topic_number=7
   if number==4 and 'voice changes during puberty' in question['question']: topic_number=3
   if number==3 and any(fragment in question['question'] for fragment in ['copying a circle','copying a square']): topic_number=6
   topic=lesson['topics'][topic_number-1]
   question.update(topicId=topic['id'],topic=topic['title'],sourceSlides=topic['slides'])
   stem=question['question'].casefold().strip()
   assert stem not in stems, f'Duplicate stem: {stem}'
   stems.add(stem)
   assert len(set(v.casefold() for v in question['options']))==4
   assert len(question['explanation'].split())>=12
  for question,topic_number in zip(lesson['questions'],BASE_TOPICS[number]):
   if question['id'] in refinements:
    wrong=iter(refinements[question['id']]);question['options']=[option if i==question['answer'] else next(wrong) for i,option in enumerate(question['options'])]
   annotate(question,topic_number)
  topic_number=None
  source=Path('question-bank')/f'lecture-{number:02}.txt'
  for row in source.read_text().splitlines():
   if not row.strip():continue
   if row.startswith('#'):
    topic_number=int(row[1:].strip());continue
   stem,correct,*rest=row.split('~')
   wrong1,wrong2,wrong3,why=rest
   ix=len(lesson['questions'])+1
   options=[correct,wrong1,wrong2,wrong3]
   random.Random(number*1000+ix).shuffle(options)
   difficulty='Applied' if any(v in stem.lower() for v in ['a child','a baby','a toddler','an infant','a caregiver','a student','a parent','an adolescent','a learner','a preschooler','a fetus','a newborn','a teacher']) else ('Analysis' if stem.startswith(('Why','How','What is a limitation','What distinguishes')) else 'Core')
   question=dict(id=f'CD{number}Q{ix:03}',lecture=number,question=stem,options=options,answer=options.index(correct),explanation=why,difficulty=difficulty)
   annotate(question,topic_number);lesson['questions'].append(question)
  assert len(lesson['questions'])==75,(number,len(lesson['questions']))
  assert all(any(q['topicId']==t['id'] for q in lesson['questions']) for t in lesson['topics'])
 assert sum(len(l['questions']) for l in lessons)==600
