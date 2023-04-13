<p><a href="https://www.beecrowd.com.br/repository/UOJ_2623_en.html">beecrowd.com.br/repository/UOJ_2623_en.html</a></p><hr>
                                  <div>
                                    <span>URI Online <strong>SQL</strong> | 2623 </span>
                                    <h1>Categories with Various Products</h1>
                                    <div>
                                      <p>Paulo R. Rodegheri <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brasil</p>
                                    </div>
                                    <strong>Timelimit: 1</strong>
                                  </div>
                                  <div>
                                  <div>
                                    <p>The sales industry needs a report to know what products are left in stock.</p>
                                    <p>To help the sales industry, display the product name and category name for products whose amount is greater than 100 and the category ID is 1,2,3,6 or 9. Show the results in ascendent order by category ID.</p>
                                  </div>
                                  <div>
                                  <h2>Schema</h2>
                                  <div>
                                  <table>
                                  <caption>products</caption>
                                  <tbody><tr>
                                  <td><strong>Column</strong></td>
                                  <td><strong>Type</strong></td>
                                </tr>
                                <tr>
                                  <td>id (PK)</td>
                                  <td>numeric</td>
                                </tr>
                                <tr>
                                  <td>name</td>
                                  <td>character varying (255)</td>
                                </tr>
                                <tr>
                                  <td>amount</td>
                                  <td>numeric</td>
                                </tr>
                                <tr>
                                  <td>price</td>
                                  <td>numeric</td>
                                </tr>
                                <tr>
                                  <td>id_categories (FK)</td>
                                  <td>numeric</td>
                                </tr>
                              </tbody></table>
                              <table>
                              <caption>categories</caption>
                              <tbody><tr>
                              <td><strong>Column</strong></td>
                              <td><strong>Type</strong></td>
                            </tr>
                            <tr>
                              <td>id (PK)</td>
                              <td>numeric</td>
                            </tr>
                            <tr>
                              <td>name</td>
                              <td>character varying (255)</td>
                            </tr>
                          </tbody></table>
                        </div>
                      </div>
                      <div>
                      <h2>Tables</h2>
                      <div>
                      <table>
                      <caption>products</caption>
                      <tbody><tr>
                      <td><strong>id</strong></td>
                      <td><strong>name</strong></td>
                      <td><strong>amount</strong></td>
                      <td><strong>price</strong></td>
                      <td><strong>id_categories</strong></td>
                    </tr>
                    <tr>
                      <td>1</td>
                      <td>Blue Chair</td>
                      <td>30</td>
                      <td>300.00</td>
                      <td>9</td>
                    </tr>
                    <tr>
                      <td>2</td>
                      <td>Red Chair</td>
                      <td>200</td>
                      <td>2150.00</td>
                      <td>2</td>
                    </tr>
                    <tr>
                      <td>3</td>
                      <td>Disney Wardrobe</td>
                      <td>400</td>
                      <td>829.50</td>
                      <td>4</td>
                    </tr>
                    <tr>
                      <td>4</td>
                      <td>Blue Toaster</td>
                      <td>20</td>
                      <td>9.90</td>
                      <td>3</td>
                    </tr>
                    <tr>
                      <td>5</td>
                      <td>Solar Panel</td>
                      <td>30</td>
                      <td>3000.25</td>
                      <td>4</td>
                    </tr>
                  </tbody></table>
                  <table>
                  <caption>categories</caption>
                  <tbody><tr>
                  <td><strong>id</strong></td>
                  <td><strong>name</strong></td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>Superior</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>Super Luxury</td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>Modern</td>
                </tr>
                <tr>
                  <td>4</td>
                  <td>Nerd</td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>Infantile</td>
                </tr>
                <tr>
                  <td>6</td>
                  <td>Robust</td>
                </tr>
                <tr>
                  <td>9</td>
                  <td>Wood</td>
                </tr>
              </tbody></table>
            </div>
          </div>
          <div>
          <h2>Output Sample</h2>
          <div>
          <table>
          <tbody><tr>
          <td><strong>name</strong></td>
          <td><strong>name</strong></td>
        </tr>
        <tr>
          <td>Red Chair</td>
          <td>Super Luxury</td>
        </tr>
      </tbody></table>
    </div>
  </div>
  <p>
  </p>
</div>