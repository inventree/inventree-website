module Jekyll
    module Drops
      class UrlDrop < Drop
        def doc_author
          @obj.data['author']
        end
      end
    end
  end