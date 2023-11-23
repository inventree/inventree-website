# see https://stackoverflow.com/a/36769049/17860466

Jekyll::Hooks.register :posts, :pre_render do |post|

    # get the current post last modified time
    modification_time = File.mtime( post.path )
  
    # inject modification_time in post's datas.
    post.data['last-modified-date'] = modification_time
  
end


Jekyll::Hooks.register :repo, :pre_render do |repo|

    # get the current post last modified time
    modification_time = File.mtime( repo.path )
  
    # inject modification_time in post's datas.
    repo.data['last-modified-date'] = modification_time
  
end